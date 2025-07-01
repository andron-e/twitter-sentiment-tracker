# dashboards/streamlit_app.py

import streamlit as st
import pandas as pd
import glob

st.title(" Twitter Sentiment Analysis Dashboard for Tech Stocks")

files = sorted(glob.glob("data/processed/*.csv"))
if not files:
    st.warning("No processed data files found. Please run the pipeline first.")
else:
    df = pd.concat([pd.read_csv(f) for f in files])
    ticker = st.selectbox("Select a stock ticker", df["ticker"].unique())
    df_filtered = df[df["ticker"] == ticker]

    st.line_chart(df_filtered.groupby(df_filtered['date'].str[:10])['compound'].mean())
    st.write(df_filtered[['date', 'content', 'compound']].tail(10))