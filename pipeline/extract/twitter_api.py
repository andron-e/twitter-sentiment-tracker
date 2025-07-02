# pipeline/extract/twitter_api.py

from dotenv import load_dotenv
import os
import tweepy
import pandas as pd

# Load .env variables
load_dotenv()

bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Authenticate with Twitter v2 API
client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweets(query, max_results=10):
    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["created_at", "text", "author_id", "lang"]
        )
        tweets = []
        if response.data:
            for tweet in response.data:
                tweets.append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "created_at": tweet.created_at,
                    "author_id": tweet.author_id,
                    "lang": tweet.lang
                })
        return tweets
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

def fetch(tickers, max_results=10):
    all_tweets = []
    for ticker in tickers:
        # Remove $ to avoid cashtag operator error, use plain ticker
        query = f"{ticker} lang:en"
        tweets = fetch_tweets(query, max_results)
        for tweet in tweets:
            all_tweets.append({
                "ticker": ticker,
                "id": tweet["id"],
                "text": tweet["text"],
                "created_at": tweet["created_at"],
                "author_id": tweet["author_id"],
                "lang": tweet["lang"]
            })
    return pd.DataFrame(all_tweets)