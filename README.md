<div align="center">

<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
<img src="https://img.shields.io/badge/yfinance-003087?style=for-the-badge&logo=yahoo&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge"/>

<br/><br/>

# 📈 Stock Trend Prediction Web App

### An AI-powered stock analysis dashboard using LSTM deep learning, real-time market data, and interactive Plotly charts — built with Streamlit.

<br/>

**[🚀 Live Demo](#quick-start) · [📸 Screenshots](#screenshots) · [⚙️ Features](#features) · [📦 Installation](#installation) · [👨‍💻 Author](#author)**

<br/>

---

</div>

<br/>

## 📸 Screenshots



### 🖥️ Full Dashboard View

<img width="1919" height="914" alt="Screenshot 2026-04-26 033417" src="https://github.com/user-attachments/assets/fc1ea974-4efc-4bd2-8bcd-d34064ac0b2d" />


*AAPL stock analysis — candlestick chart with Bollinger Bands, MACD, and RSI indicators over 3 years*

</div>

<br/>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 AI & Machine Learning
- **Stacked LSTM** neural network (2-layer architecture)
- **Configurable lookback window** — default 60 days
- **EarlyStopping + ReduceLROnPlateau** callbacks for smart training
- **7–30 day iterative forecasting** with confidence band
- **CPU-optimized** — works on any laptop without a GPU

</td>
<td width="50%">

### 📊 Technical Analysis
- **RSI (14-period)** — overbought/oversold signals
- **MACD** — momentum and trend direction
- **Bollinger Bands** — volatility and price channels
- **SMA-20, SMA-50, EMA-20** — trend support levels
- **Volume analysis** — color-coded buy/sell pressure

</td>
</tr>
<tr>
<td width="50%">

### 📡 Data & Performance
- **Live data** via `yfinance` — any Yahoo Finance ticker
- **Global stocks** — US, Indian (`.NS`), UK (`.L`), and more
- **`@st.cache_data`** caching — no redundant API calls
- **3+ years of historical OHLCV** data by default
- **Auto date range** — sensible defaults on first load

</td>
<td width="50%">

### 🎨 Dashboard & UI
- **Dark theme** interactive Plotly charts
- **Sentiment indicator** — Bullish 🟢 / Bearish 🔴 / Neutral 🟡
- **Model metrics** — RMSE, MAE, R², MAPE on test set
- **Forecast table** — daily predicted prices with % change
- **CSV download** — one-click export of predictions + raw data

</td>
</tr>
</table>

<br/>

---

## 🏗️ Project Architecture

```
stock_app/
│
├── 📄 app.py              ← Streamlit UI — sidebar, charts, metrics, downloads
├── 🗃️ data_loader.py      ← yfinance fetch + technical indicator computation
├── 🧠 model.py            ← LSTM architecture, training pipeline, forecasting
├── 🛠️ utils.py            ← Plotly charts, sentiment logic, CSV export helpers
├── 📋 requirements.txt    ← All Python dependencies
└── 📖 README.md
```

### Data Flow

```
User Input (Ticker + Date Range)
        ↓
  data_loader.py
  ├── yfinance download (OHLCV)
  ├── RSI / MACD / Bollinger Bands
  └── @st.cache_data (session cache)
        ↓
    model.py
  ├── MinMaxScaler normalization
  ├── Sliding window sequences
  ├── LSTM (64→32 units) + Dropout
  ├── EarlyStopping (patience=8)
  └── Iterative N-day forecast
        ↓
    utils.py
  ├── Plotly candlestick + overlays
  ├── Sentiment score
  └── CSV builder
        ↓
    app.py → Streamlit Dashboard
```

<br/>

---

## 📦 Installation

### Prerequisites

- Python **3.10** or **3.11**
- pip
- Internet connection (for yfinance)

### Step 1 — Clone the repository

```bash
git clone https://github.com/ADARSH685-BOT/Stock-Trend-Prediction-Web-App.git
cd Stock-Trend-Prediction-Web-App
```

### Step 2 — Create a virtual environment

```bash
# Create
python -m venv .venv

# Activate (Mac/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

> ⏳ First install takes ~3–5 minutes (TensorFlow is ~500 MB)

### Step 4 — Run the app

```bash
streamlit run app.py
```

Open **[http://localhost:8501](http://localhost:8501)** in your browser. 🎉

<br/>

---

## 🚀 Quick Start

Once the app is running:

| Step | Action |
|------|--------|
| 1️⃣ | Enter a stock ticker in the sidebar — e.g. `AAPL`, `TSLA`, `MSFT`, `RELIANCE.NS` |
| 2️⃣ | Select your date range (default: last 3 years) |
| 3️⃣ | Adjust model parameters if needed (defaults work great) |
| 4️⃣ | Click **🚀 Analyze & Predict** |
| 5️⃣ | Explore the interactive charts, metrics, and forecast table |
| 6️⃣ | Download your forecast as CSV |

### 🌍 Supported Ticker Formats

| Market | Example Tickers |
|--------|----------------|
| 🇺🇸 US Stocks | `AAPL`, `TSLA`, `MSFT`, `GOOGL`, `NVDA` |
| 🇮🇳 Indian NSE | `RELIANCE.NS`, `TCS.NS`, `INFY.NS`, `HDFCBANK.NS` |
| 🇬🇧 London Stock Exchange | `BARC.L`, `SHEL.L`, `AZN.L` |
| 📊 Indices | `^NSEI` (Nifty 50), `^BSESN` (Sensex), `^GSPC` (S&P 500) |
| ₿ Crypto | `BTC-USD`, `ETH-USD`, `SOL-USD` |

<br/>

---

## ⚙️ Sidebar Controls

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| **Stock Ticker** | `AAPL` | Any valid symbol | Yahoo Finance ticker symbol |
| **Start Date** | 3 years ago | 2000–today | Beginning of training data |
| **End Date** | Today | — | End of training data |
| **Lookback Window** | `60` days | 20–120 | Past days per LSTM input step |
| **LSTM Epochs** | `50` | 10–150 | Max training iterations (EarlyStopping may reduce) |
| **LSTM Units** | `64` | 32/64/96/128 | Neurons in the first LSTM layer |
| **Dropout Rate** | `0.2` | 0.1–0.5 | Regularization between layers |
| **Forecast Horizon** | `7` days | 3–30 | Number of future business days to predict |

<br/>

---

## 📐 Model Details

### LSTM Architecture

```
Input  →  (lookback, 1)
           │
    ┌──────▼──────┐
    │  LSTM (64)  │  return_sequences=True
    └──────┬──────┘
    ┌──────▼──────┐
    │  Dropout    │  rate=0.2
    └──────┬──────┘
    ┌──────▼──────┐
    │  LSTM (32)  │  return_sequences=False
    └──────┬──────┘
    ┌──────▼──────┐
    │  Dropout    │  rate=0.2
    └──────┬──────┘
    ┌──────▼──────┐
    │  Dense (25) │  ReLU activation
    └──────┬──────┘
    ┌──────▼──────┐
    │  Dense (1)  │  Linear output
    └─────────────┘
           │
        Close Price Prediction
```

### Training Strategy
- **Optimizer:** Adam
- **Loss:** Mean Squared Error
- **Train/Test split:** 80% / 20%
- **EarlyStopping:** patience=8, monitors `val_loss`
- **ReduceLROnPlateau:** factor=0.5, patience=4
- **Forecasting:** Iterative (each predicted step feeds into the next)

<br/>

---

## 📊 Output Metrics

| Metric | Description |
|--------|-------------|
| **RMSE** | Root Mean Squared Error — average prediction error in $ |
| **MAE** | Mean Absolute Error — average absolute deviation |
| **R²** | Coefficient of determination — how well model fits data (1.0 = perfect) |
| **MAPE** | Mean Absolute Percentage Error — error as a percentage |
| **Sentiment** | Bullish / Bearish / Neutral based on predicted price trajectory |

<br/>

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` in your activated venv |
| `No data for ticker` | Check spelling — Indian stocks need `.NS` suffix (e.g. `TCS.NS`) |
| Slow training | Reduce **Epochs** to 20 in the sidebar; LSTM on CPU takes 1–3 min |
| Port already in use | `streamlit run app.py --server.port 8502` |
| yfinance timeout | Check your internet connection and retry |
| `Not enough data` | Extend the date range or reduce the Lookback Window |

<br/>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **UI Framework** | Streamlit 1.32+ |
| **Deep Learning** | TensorFlow / Keras (LSTM) |
| **Data Source** | yfinance (Yahoo Finance API) |
| **Visualization** | Plotly 5.x (dark theme) |
| **Data Processing** | Pandas, NumPy |
| **ML Utilities** | scikit-learn (scaling, metrics) |
| **Language** | Python 3.10+ |

</div>

<br/>

---

## ⚠️ Disclaimer

> This application is built **for educational and research purposes only**.
> Stock price predictions made by LSTM or any ML model are **not financial advice**.
> Past performance does not guarantee future results.
> Always consult a licensed financial advisor before making investment decisions.

<br/>

---

## 👨‍💻 Author

<div align="center">

<img src="https://avatars.githubusercontent.com/ADARSH685-BOT" width="100" style="border-radius:50%"/>

### Adarsh Kumar

[![GitHub](https://img.shields.io/badge/GitHub-ADARSH685--BOT-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ADARSH685-BOT)
[![Repository](https://img.shields.io/badge/Repo-Stock--Trend--Prediction-22c55e?style=for-the-badge&logo=github)](https://github.com/ADARSH685-BOT/Stock-Trend-Prediction-Web-App)

*Built with ❤️ using Python, TensorFlow & Streamlit*

</div>

<br/>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
<img width="1919" height="914" alt="Screenshot 2026-04-26 033417" src="https://github.com/user-attachments/assets/d8664ac6-1e35-42ab-a05d-15d5ff89b43f" />


⭐ **If you found this project helpful, please give it a star!** ⭐

[![Star this repo](https://img.shields.io/github/stars/ADARSH685-BOT/Stock-Trend-Prediction-Web-App?style=social)](https://github.com/ADARSH685-BOT/Stock-Trend-Prediction-Web-App)

</div>
