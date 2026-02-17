📈 Apple Stock Price Forecasting using SARIMA

A Time Series Forecasting & Deployment Project

📌 1. Project Overview

This project focuses on building a time series forecasting model to predict future stock prices of Apple Inc. using historical stock market data.

The primary objective is to:

Analyze historical Apple stock price trends

Build a statistical forecasting model

Generate 30-day future predictions

Deploy the trained model using Streamlit

Provide an interactive web interface for users

The forecasting model used in this project is:

SARIMA (Seasonal AutoRegressive Integrated Moving Average)

The model is trained on historical stock data and deployed as a web application for real-time prediction without retraining.

📊 2. Dataset Description

The dataset contains historical Apple stock market data including:

Date

Open Price

High Price

Low Price

Close Price

Volume

Data Used For Training:

Historical stock prices from 2012 to 2019

Target Variable:

Close price (Closing stock price)

📂 3. Project Structure
Apple-Stock-Forecasting/
│
├── Apple_Stock_Analysis.ipynb
├── AppleStockModelDeployment.ipynb
├── AppleStockModelDeployment.py
├── Appledataset.csv
├── sarima_model.pkl
├── requirements.txt
└── README.md

File Explanation
File	Description
Apple_Stock_Analysis.ipynb	Data cleaning, EDA, stationarity tests, model training
AppleStockModelDeployment.py	Streamlit application
Appledataset.csv	Historical stock dataset
sarima_model.pkl	Trained SARIMA model
requirements.txt	Required Python libraries
README.md	Project documentation
🔎 4. Exploratory Data Analysis (EDA)

Before building the forecasting model, several analytical steps were performed:

✔ Data Cleaning

Converted Date column to datetime format

Set date as index

Checked for missing values

Sorted data chronologically

✔ Trend Analysis

Visualized historical closing prices

Observed long-term upward trend

Identified seasonal fluctuations

✔ Stationarity Check

Since time series models require stationary data:

Applied ADF (Augmented Dickey-Fuller) Test

Performed differencing to remove trend

Applied seasonal differencing for seasonality

🤖 5. Model Used: SARIMA
🔹 What is ARIMA?

ARIMA stands for:

AR (AutoRegressive) – Uses previous values

I (Integrated) – Differencing to make series stationary

MA (Moving Average) – Uses previous error terms

ARIMA is defined as:

ARIMA(p, d, q)


Where:

p → Number of lag observations

d → Degree of differencing

q → Size of moving average window

🔹 What is SARIMA?

SARIMA extends ARIMA to handle seasonality.

It is defined as:

SARIMA(p, d, q)(P, D, Q, s)


Where:

(p, d, q) → Non-seasonal parameters

(P, D, Q, s) → Seasonal parameters

s → Length of seasonal cycle

Why SARIMA?

Stock prices often show:

Trends

Cyclical behavior

Seasonal movement

SARIMA effectively captures:

Trend

Seasonality

Auto-correlation patterns

⚙️ 6. Model Training Process

Checked stationarity using ADF test

Applied differencing to remove trend

Used ACF and PACF plots to determine p and q

Selected optimal seasonal parameters

Trained SARIMA model using statsmodels

Evaluated using:

AIC score

Residual diagnostics

Saved trained model using Pickle:

pickle.dump(model, open("sarima_model.pkl", "wb"))

📈 7. Forecasting Strategy

The model generates:

Future stock predictions for user-selected dates

Maximum next 30 days forecast

Business-day frequency forecasting

Forecast Generation Code
forecast = model.forecast(steps=forecast_days)


Predictions are displayed as:

Data table

Line graph comparison (Historical vs Forecasted)

🌐 8. Deployment Using Streamlit

The trained model is deployed using Streamlit, which allows:

Interactive UI

Real-time forecasting

User-selected date range

Automatic prediction generation

App Features

Historical trend visualization

Date range input selection

Dynamic forecast generation

Interactive visualization

Tabular output display

Run the app using:

streamlit run AppleStockModelDeployment.py

🛠 9. Technologies Used

Python

Pandas

NumPy

Matplotlib

Statsmodels

Scikit-learn

Streamlit

Pickle

📊 10. Model Evaluation

Model performance was evaluated using:

Residual analysis

AIC score minimization

Visual inspection of forecast consistency

Comparison with historical trends

Lower AIC indicates better model fit.

🚀 11. How to Run the Project
Step 1: Clone Repository
git clone https://github.com/your-username/Apple-Stock-Forecasting.git
cd Apple-Stock-Forecasting

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run Application
streamlit run AppleStockModelDeployment.py

🎯 12. Key Learnings

Through this project, I gained hands-on experience in:

Time series data preprocessing

Stationarity testing

SARIMA parameter tuning

Model persistence using Pickle

Web app deployment using Streamlit

Forecast visualization

⚠️ 13. Limitations

Model is based only on historical prices

Does not include:

Market news

Economic indicators

Company fundamentals

Forecast limited to 30 days

Financial markets are highly volatile

🔮 14. Future Improvements

Implement Prophet model

Compare with LSTM deep learning model

Add confidence intervals visualization

Deploy using Streamlit Cloud

Automate real-time data fetching

👨‍💻 Author

Praveen Poluri
Data Science & Machine Learning Enthusiast
