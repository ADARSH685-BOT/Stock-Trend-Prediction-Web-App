import streamlit as st
import pandas as pd
from datetime import date, timedelta
from data_loader import fetch_data, compute_technical_indicators
from model import prepare_data, build_and_train_model, predict_future, evaluate_model
from utils import plot_candlestick_with_indicators, plot_predictions, get_sentiment
import warnings
import datetime
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Stock Trend Predictor", layout="wide", page_icon="📈")

st.title("📈 Stock Trend Prediction & Analysis Dashboard")

# --- Sidebar Controls ---
st.sidebar.header("User Input Options")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL").upper()
start_date = st.sidebar.date_input("Start Date", date.today() - timedelta(days=365*3))
end_date = st.sidebar.date_input("End Date", date.today())

st.sidebar.subheader("Model Parameters")
lookback = st.sidebar.slider("Lookback Window (Days)", 30, 100, 60)
epochs = st.sidebar.slider("LSTM Epochs", 5, 50, 10)
future_days = st.sidebar.slider("Days to Predict", 1, 30, 7)

if start_date >= end_date:
    st.sidebar.error("Error: End date must fall after start date.")
    st.stop()

# --- Main Flow ---
if st.sidebar.button("Analyze & Predict"):
    with st.spinner(f"Fetching data for {ticker}..."):
        df_raw = fetch_data(ticker, start_date, end_date)
        
    if df_raw is None or df_raw.empty:
        st.error(f"Failed to fetch data for {ticker}. Please check the ticker symbol and date range.")
    else:
        st.success("Data loaded successfully!")
        
        # Technical Indicators
        df_ta = compute_technical_indicators(df_raw)
        
        # Tabs for layout
        tab1, tab2, tab3 = st.tabs(["📊 Technical Analysis", "🔮 Predictions", "💾 Data Download"])
        
        with tab1:
            st.subheader(f"{ticker} Technical Analysis")
            fig_ta = plot_candlestick_with_indicators(df_ta, ticker)
            st.plotly_chart(fig_ta, use_container_width=True)
            
        with tab2:
            st.subheader("LSTM Model Prediction")
            
            # Prepare data and model
            x_train, y_train, scaler, raw_close_data = prepare_data(df_ta, lookback)
            model = build_and_train_model(x_train, y_train, epochs=epochs)
            
            # Evaluation
            rmse, mae, r2, _, _ = evaluate_model(model, scaler, raw_close_data, lookback)
            
            if rmse is not None:
                st.write("### Model Performance Metrics")
                col1, col2, col3 = st.columns(3)
                col1.metric("RMSE", f"{rmse:.2f}")
                col2.metric("MAE", f"{mae:.2f}")
                col3.metric("R² Score", f"{r2:.4f}")
            
            # Future Prediction
            with st.spinner(f"Predicting next {future_days} days..."):
                future_preds = predict_future(model, scaler, raw_close_data, lookback, future_days)
            
            # Dates for prediction
            last_date = df_ta.index[-1]
            next_dates = []
            curr_date = last_date
            while len(next_dates) < future_days:
                curr_date += timedelta(days=1)
                if curr_date.weekday() < 5:
                    next_dates.append(curr_date)
            
            # Plot future predictions
            fig_pred = plot_predictions(df_ta, future_preds, next_dates)
            st.plotly_chart(fig_pred, use_container_width=True)
            
            # Sentiment Analysis
            sentiment, color, change = get_sentiment(future_preds)
            st.markdown(f"### Predicted Trend Sentiment: <span style='color:{color}'>{sentiment} ({change:.2f}%)</span>", unsafe_allow_html=True)
            
        with tab3:
            st.subheader("Download Data")
            pred_df = pd.DataFrame({'Date': next_dates, 'Predicted_Close': future_preds})
            st.dataframe(pred_df)
            
            csv = pred_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Predictions as CSV",
                data=csv,
                file_name=f'{ticker}_predictions.csv',
                mime='text/csv',
            )
else:
    st.info("Please click 'Analyze & Predict' from the sidebar to begin.")
