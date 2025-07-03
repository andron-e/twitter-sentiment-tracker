import pandas as pd
from datetime import datetime

def save(df):
    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if "ticker" not in df.columns or df.empty:
        print("Warning: No 'ticker' column found or DataFrame is empty in to_csv.save. No files will be written.")
        return
    for ticker in df["ticker"].unique():
        ticker_df = df[df["ticker"] == ticker]
        ticker_df.to_csv(f"data/processed/{ticker}_{timestamp_str}.csv", index=False)