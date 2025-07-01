# Add at top of run_pipeline.py
import logging
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)
logging.info("Pipeline started")

from pipeline.extract import twitter_api, scrape_news
from pipeline.transform import clean_text, sentiment_analysis
from pipeline.load import to_csv

def main():
    tweets = twitter_api.fetch(tickers=["TSLA", "AAPL"])
    news = scrape_news.fetch(["TSLA", "AAPL"])
    raw_data = tweets + news

    cleaned = clean_text.process(raw_data)
    scored = sentiment_analysis.apply(cleaned)

    to_csv.save(scored)

if __name__ == "__main__":
    main()