import pandas as pd
from datetime import datetime

def save(df):
    date_str = datetime.now().strftime("%Y-%m-%d")
    for ticker in df["ticker"].unique():
        ticker_df = df[df["ticker"] == ticker]
        ticker_df.to_csv(f"data/processed/{ticker}_{date_str}.csv", index=False)