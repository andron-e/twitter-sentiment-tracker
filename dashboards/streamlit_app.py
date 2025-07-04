# dashboards/streamlit_app.py

import streamlit as st
import pandas as pd
import glob
from sklearn.linear_model import LinearRegression
import numpy as np
import subprocess

st.title("Twitter Sentiment Analysis Dashboard for Tech Stocks")

# Button to run the pipeline and generate new processed data
if st.button("Run Pipeline Now"):
    with st.spinner("Running pipeline..."):
        result = subprocess.run(["python", "run_pipeline.py"], capture_output=True, text=True)
        st.success("Pipeline completed!")
        st.text(result.stdout)
        st.text(result.stderr)

files = sorted(glob.glob("data/processed/*.csv"))
if not files:
    st.warning("No processed data files found. Please run the pipeline first.")
else:
    df = pd.concat([pd.read_csv(f) for f in files])
    ticker = st.selectbox("Select a stock ticker", df["ticker"].unique())
    df_filtered = df[df["ticker"] == ticker].copy()

    # Convert created_at to datetime and sort
    df_filtered["created_at"] = pd.to_datetime(df_filtered["created_at"])
    df_filtered = df_filtered.sort_values("created_at")

    # Sentiment trend over time (count of each sentiment per day)
    df_filtered["date"] = df_filtered["created_at"].dt.date
    sentiment_counts = df_filtered.groupby(["date", "sentiment"]).size().unstack(fill_value=0)
    st.subheader("Sentiment Trend Over Time")
    st.line_chart(sentiment_counts)

    # Show recent tweets
    st.subheader("Recent Tweets")
    st.write(df_filtered[["created_at", "text", "sentiment"]].tail(10))

    # Simple sentiment forecasting using linear regression
    st.subheader("Sentiment Forecast (Linear Trend)")
    # We'll forecast the count of positive tweets
    if "positive" in sentiment_counts.columns and len(sentiment_counts) > 1:
        X = np.arange(len(sentiment_counts)).reshape(-1, 1)
        y = sentiment_counts["positive"].values
        model = LinearRegression().fit(X, y)
        y_pred = model.predict(X)
        st.line_chart({"Actual Positive": y, "Forecasted Trend": y_pred})
        st.write(f"Forecasted next day's positive sentiment count: {int(model.predict([[len(sentiment_counts)]]).item())}")
    else:
        st.info("Not enough positive sentiment data for forecasting.")