import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import streamlit as st

def prepare_data(df, lookback=60):
    """
    Prepare data for LSTM model.
    """
    data = df.filter(['Close']).values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    
    x_train, y_train = [], []
    for i in range(lookback, len(scaled_data)):
        x_train.append(scaled_data[i-lookback:i, 0])
        y_train.append(scaled_data[i, 0])
        
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    
    return x_train, y_train, scaler, data

def build_and_train_model(x_train, y_train, epochs=10, batch_size=32):
    """
    Build and train the LSTM model.
    """
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Train the model
    with st.spinner("Training LSTM model... This may take a moment."):
        model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=0)
        
    return model

def predict_future(model, scaler, data, lookback=60, days=7):
    """
    Predict future prices using the trained LSTM model.
    """
    future_predictions = []
    last_60_days = data[-lookback:]
    last_60_days_scaled = scaler.transform(last_60_days)
    
    x_test = []
    x_test.append(last_60_days_scaled)
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    
    for _ in range(days):
        pred_price = model.predict(x_test, verbose=0)
        future_predictions.append(pred_price[0,0])
        
        # update x_test for next prediction
        pred_price_reshaped = np.reshape(pred_price, (1, 1, 1))
        x_test = np.append(x_test[:, 1:, :], pred_price_reshaped, axis=1)
        
    future_predictions = np.array(future_predictions).reshape(-1, 1)
    future_predictions = scaler.inverse_transform(future_predictions)
    return future_predictions.flatten()

def evaluate_model(model, scaler, data, lookback=60):
    """
    Evaluate the model on the available data.
    """
    train_data_len = int(np.ceil(len(data) * 0.8))
    
    scaled_data = scaler.transform(data)
    test_data = scaled_data[train_data_len - lookback: , :]
    
    x_test = []
    y_test = data[train_data_len:, :]
    for i in range(lookback, len(test_data)):
        x_test.append(test_data[i-lookback:i, 0])
        
    x_test = np.array(x_test)
    if x_test.shape[0] > 0:
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        predictions = model.predict(x_test, verbose=0)
        predictions = scaler.inverse_transform(predictions)
        
        # metrics
        from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        return rmse, mae, r2, predictions, train_data_len
    return None, None, None, None, None
