import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def plot_candlestick_with_indicators(df, ticker):
    """
    Plot interactive candlestick chart with RSI, MACD, and Bollinger Bands.
    """
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.03, subplot_titles=(f'{ticker} Price & Bollinger Bands', 'MACD', 'RSI'),
                        row_width=[0.2, 0.2, 0.6])

    # Candlestick
    fig.add_trace(go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='OHLC'),
                  row=1, col=1)

    # Bollinger Bands
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_High'], line=dict(color='gray', width=1, dash='dash'), name='BB High'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_Low'], line=dict(color='gray', width=1, dash='dash'), name='BB Low', fill='tonexty'), row=1, col=1)

    # MACD
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], line=dict(color='blue', width=2), name='MACD'), row=2, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD_Signal'], line=dict(color='orange', width=2), name='Signal'), row=2, col=1)
    
    # MACD Histogram
    colors = ['green' if val >= 0 else 'red' for val in (df['MACD'] - df['MACD_Signal'])]
    fig.add_trace(go.Bar(x=df.index, y=df['MACD'] - df['MACD_Signal'], marker_color=colors, name='MACD Hist'), row=2, col=1)

    # RSI
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='purple', width=2), name='RSI'), row=3, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=3, col=1)

    fig.update_layout(height=800, xaxis_rangeslider_visible=False, template='plotly_dark')
    return fig

def plot_predictions(data, predictions_future, next_days_dates):
    """
    Plot actual vs predicted future prices.
    """
    fig = go.Figure()
    
    # Plot last 60 days of actual data
    last_60 = data[-60:]
    fig.add_trace(go.Scatter(x=last_60.index, y=last_60['Close'], mode='lines', name='Actual Close Price'))
    
    # Plot predicted future data
    fig.add_trace(go.Scatter(x=next_days_dates, y=predictions_future, mode='lines+markers', name='Predicted Close Price', line=dict(color='red', dash='dash')))
    
    fig.update_layout(title='Future Price Prediction', xaxis_title='Date', yaxis_title='Price', template='plotly_dark')
    return fig

def get_sentiment(predictions):
    """
    Determine sentiment based on predicted trend.
    """
    start_price = predictions[0]
    end_price = predictions[-1]
    change = ((end_price - start_price) / start_price) * 100
    
    if change > 2:
        return "BULLISH 🚀", "green", change
    elif change < -2:
        return "BEARISH 📉", "red", change
    else:
        return "NEUTRAL ↔️", "gray", change
