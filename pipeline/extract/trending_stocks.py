def get_trending(limit=5):
    # Static fallback: returns example trending tickers
    example_tickers = ["TSLA", "AAPL", "NVDA", "AMZN", "GOOGL"]
    return example_tickers[:limit]