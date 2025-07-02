from pipeline.extract.twitter_api import fetch_tweets

if __name__ == "__main__":
    query = "$TSLA lang:en"
    tweets = fetch_tweets(query, max_results=10)
    if not tweets:
        print("No tweets fetched or an error occurred.")
        print("If you see a '429 Too Many Requests' error, you have hit the Twitter API rate limit. Wait 15-30 minutes before trying again, or apply for Elevated access if needed.")
    else:
        for tweet in tweets:
            print(f"{tweet['created_at']} | {tweet['author_id']}: {tweet['text'][:100]}...")
