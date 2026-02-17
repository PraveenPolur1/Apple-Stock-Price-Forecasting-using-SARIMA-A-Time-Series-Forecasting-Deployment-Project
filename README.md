# 📈 Apple Stock Price Forecasting using SARIMA  
### End-to-End Time Series Modeling & Streamlit Deployment

---

## 🚀 Live Project Overview

This project builds a **statistical time series forecasting system** to predict future stock prices of Apple Inc. (AAPL) using the **SARIMA model**, and deploys it via an interactive **Streamlit web application**.

It demonstrates:

- 📊 Exploratory Data Analysis (EDA)
- 🔬 Stationarity Testing & Differencing
- 📈 ACF/PACF-based Parameter Selection
- 🤖 SARIMA Model Training
- 💾 Model Serialization with Pickle
- 🌐 Web App Deployment using Streamlit
- 📅 Dynamic Future Forecast Generation

---

# 📌 Business Problem

Financial markets are dynamic and volatile. Investors require reliable forecasting methods to:

- Understand historical trends
- Predict short-term price movement
- Support investment decision-making

This project answers:

> Can historical Apple stock data be used to statistically forecast future prices using classical time series modeling?

---

# 🧠 Why SARIMA?

Stock prices often show:

- Long-term trends
- Autocorrelation patterns
- Seasonal fluctuations
- Non-stationary behavior

A simple linear model cannot capture these patterns effectively.

SARIMA was selected because it:

✔ Handles non-stationary time series  
✔ Models autocorrelation  
✔ Captures seasonality  
✔ Works well for short-term financial forecasting  

---

# 📊 Dataset Description

**Source:** Historical Apple stock price dataset  
**Time Period:** 2012 – 2019  
**Frequency:** Daily  

### Features:

| Feature | Description |
|----------|-------------|
| Date | Trading date |
| Open | Opening price |
| High | Highest price |
| Low | Lowest price |
| Close | Closing price (Target Variable) |
| Volume | Trading volume |

### Target Variable:
📌 `Close` Price

---

# 🔎 Exploratory Data Analysis (EDA)

## 1️⃣ Data Cleaning

- Converted Date to datetime format
- Set Date as index
- Checked missing values
- Sorted chronologically

## 2️⃣ Trend Analysis

- Observed upward long-term trend
- Identified volatility clusters
- Detected cyclical movement

## 3️⃣ Stationarity Testing

Time series models require stationary data.

### Augmented Dickey-Fuller (ADF) Test

Hypothesis:

- H₀ → Time series is non-stationary
- H₁ → Time series is stationary

After differencing:
- Achieved stationarity
- Removed trend component

---

# 📐 Model Architecture

## 🔹 ARIMA Model

ARIMA(p, d, q)

Where:

- **p** → Autoregressive terms
- **d** → Differencing order
- **q** → Moving average terms

---

## 🔹 SARIMA Model

SARIMA(p, d, q)(P, D, Q, s)

Where:

- (p, d, q) → Non-seasonal parameters
- (P, D, Q) → Seasonal parameters
- s → Seasonal cycle length

---

# 🧮 Mathematical Representation

The SARIMA model can be expressed as:

Φₚ(B) Φₚₛ(Bˢ) (1 − B)ᵈ (1 − Bˢ)ᴰ Yₜ = Θ_q(B) Θ_Q(Bˢ) εₜ

Where:

- B → Backshift operator
- Φ → AR parameters
- Θ → MA parameters
- εₜ → White noise

This allows the model to:

- Learn past dependencies
- Remove trends
- Capture repeating seasonal patterns

---

# ⚙️ Model Training Process

### Step 1: Stationarity Check  
### Step 2: Differencing  
### Step 3: ACF & PACF Analysis  
### Step 4: Parameter Selection  
### Step 5: Model Fitting (statsmodels)  
### Step 6: Residual Diagnostics  
### Step 7: Model Serialization  

```python
pickle.dump(model, open("sarima_model.pkl", "wb"))
```

---

# 📉 Model Evaluation

Evaluated using:

- AIC (Akaike Information Criterion)
- Residual white noise check
- Forecast consistency with historical trends

### Why AIC?

Lower AIC = Better model balance between:
- Complexity
- Goodness of fit

---

# 🔮 Forecasting Strategy

The deployed model:

- Accepts user-defined future date range
- Generates up to 30-day forecast
- Uses business-day frequency
- Displays:
  - Forecast table
  - Historical vs predicted graph

Core Forecast Code:

```python
forecast = model.forecast(steps=forecast_days)
```

---

# 🌐 Streamlit Deployment

The trained model is deployed using Streamlit to provide:

✔ Interactive UI  
✔ Date selection  
✔ Real-time predictions  
✔ Visual comparison plots  
✔ No retraining required  

Run locally:

```bash
streamlit run AppleStockModelDeployment.py
```

---

# 📂 Project Structure

```
Apple-Stock-Forecasting/
│
├── Apple_Stock_Analysis.ipynb        # EDA & Model Development
├── AppleStockModelDeployment.py      # Streamlit App
├── Appledataset.csv                  # Historical Data                 
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Scikit-learn
- Streamlit
- Pickle

---

# 📈 Key Skills Demonstrated

✅ Time Series Forecasting  
✅ Statistical Modeling  
✅ Stationarity Testing  
✅ Model Optimization  
✅ Data Visualization  
✅ Model Serialization  
✅ Web App Deployment  
✅ End-to-End ML Workflow  

---

# ⚠️ Limitations

- Based purely on historical prices
- Does not include:
  - Market news
  - Macroeconomic indicators
  - Sentiment data
- Limited to short-term forecasting
- Financial markets are inherently volatile

---

# 🔮 Future Improvements

- Add Prophet model comparison
- Integrate LSTM deep learning model
- Include confidence intervals
- Fetch live data using APIs
- Deploy on Streamlit Cloud
- Dockerize the project

---

# 🎯 Interview Discussion Points

- Why SARIMA over LSTM?
- How stationarity affects forecasting
- ACF vs PACF interpretation
- Model selection using AIC
- Bias-variance tradeoff in time series
- Limitations of statistical forecasting

---

# 👨‍💻 Author

**Praveen Poluri**  
Machine Learning & Data Science Enthusiast  

---

# ⭐ If you found this project valuable, consider giving it a star!
