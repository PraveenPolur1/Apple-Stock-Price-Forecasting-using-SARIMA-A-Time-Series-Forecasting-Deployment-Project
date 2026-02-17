#!/usr/bin/env python
# coding: utf-8

# ## Objective:
# 
# - The primary objective of deployment is to make the trained stock price forecasting model accessible through an interactive web application, enabling users to generate future Apple stock price predictions easily without technical expertise.
# 
# #### The deployment aims to:
# 
# - Allow users to select a **future date range and obtain next 30-day stock price forecasts**.
# 
# - Provide *interactive visualizations of historical stock trends* and predicted prices.
# 
# - Enable *real-time prediction* generation using a **pre-trained SARIMA model** without retraining.
# 
# - Present forecasting results in a **simple, user-friendly, and interpretable interface** to support informed financial decision-making.

# ### Apple Stock Price Forecasting – Streamlit App

# In[3]:


# Apple Stock Price Forecasting – Streamlit App

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Page Configuration

st.set_page_config(
    page_title="Apple Stock Forecasting",
    page_icon="📈",
    layout="centered"
)


# Title & Description

st.title("📈 Apple Stock Price Forecasting")
st.write("""
This interactive web application allows users to select a **future date range**
and obtain **predicted Apple stock closing prices for the next 30 days**.
The predictions are generated using a **SARIMA time series forecasting model**
trained on historical data (2012–2019).
""")

st.markdown("---")


# Load Historical Stock Data
@st.cache_data
def load_data():
    df = pd.read_csv("Appledataset.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

df = load_data()


# Load Trained SARIMA Model
@st.cache_resource
def load_model():
    with open("sarima_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()


# Historical Trend Visualization
st.subheader("📊 Historical Stock Price Trend")
st.line_chart(df['Close'])

st.markdown("---")


# User Input – Forecast Date Range

st.subheader("🔮 Select Forecast Date Range")

last_date = df.index[-1]

start_date = st.date_input(
    "Forecast Start Date",
    last_date + pd.Timedelta(days=1)
)

end_date = st.date_input(
    "Forecast End Date",
    last_date + pd.Timedelta(days=30)
)


# Generate Forecast
if start_date > end_date:
    st.error("❌ End date must be after start date.")

else:
    forecast_days = (end_date - start_date).days + 1

    if st.button("Generate Forecast"):
        
        # Generate future forecast
        forecast = model.forecast(steps=forecast_days)

        # Generate future business dates
        future_dates = pd.date_range(
            start=start_date,
            periods=forecast_days,
            freq='B'
        )

        forecast_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted Closing Price": forecast
        }).set_index("Date")

       
        # Display Forecast Table
        st.subheader("📋 Predicted Stock Prices")
        st.dataframe(forecast_df)

        # Forecast Visualization
        st.subheader("📈 Historical vs Forecasted Prices")

        fig, ax = plt.subplots(figsize=(10,4))
        ax.plot(df['Close'].tail(60), label="Historical Prices")
        ax.plot(forecast_df, label="Forecasted Prices", color="red")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.set_title("Apple Stock Price Forecast")
        ax.legend()
        st.pyplot(fig)


# In[ ]:




