import logging
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)
logging.info("Pipeline started")

from pipeline.extract import twitter_api, scrape_news
from pipeline.transform import clean_text, sentiment_analysis
from pipeline.load import to_csv
from pipeline.extract import trending_stocks

def main():
    tickers = trending_stocks.get_trending(limit=3)
    print("Tracking:", tickers)
    df = twitter_api.fetch(tickers, max_results=50)
    df = clean_text.clean_text(df)
    df = sentiment_analysis.apply(df)
    to_csv.save(df)

if __name__ == "__main__":
    main()
    print("Pipeline completed. Check data/processed/ for output.")