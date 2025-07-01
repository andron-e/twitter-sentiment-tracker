# pipeline/extract/twitter_api.py

import snscrape.modules.twitter as sntwitter
import pandas as pd

def fetch(tickers, max_results=100):
    all_data = []

    for ticker in tickers:
        query = f"${ticker} lang:en"
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= max_results:
                break
            all_data.append({
                "ticker": ticker,
                "date": tweet.date,
                "content": tweet.content,
                "username": tweet.user.username
            })

    return pd.DataFrame(all_data)

from twitter_api import fetch
df = fetch(["TSLA", "AAPL"], 50)
print(df.head())