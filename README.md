# Stock Trend Prediction Web App

A complete Stock Trend Prediction Web App built with Python, Streamlit, LSTM, yfinance, and Plotly.

## Features
- **Data Fetching:** Real-time historical OHLCV data using `yfinance`.
- **Technical Indicators:** Computes RSI, MACD, and Bollinger Bands.
- **Machine Learning:** Uses a Long Short-Term Memory (LSTM) neural network built with TensorFlow/Keras to predict future stock prices.
- **Interactive Visualizations:** Employs `Plotly` for interactive candlestick charts and technical indicator subplots.
- **Metrics & Sentiment:** Displays model evaluation metrics (RMSE, MAE, R²) and an overall trend sentiment (Bullish/Bearish/Neutral).
- **Export:** Download predicted future data as a CSV.

## Setup Instructions

1. Ensure you have Python 3.8+ installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Screenshots
*(Add your screenshots here)*
