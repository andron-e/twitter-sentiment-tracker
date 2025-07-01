# pipeline/transform/sentiment_analysis.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

def apply(df):
    sentiments = df["content"].apply(lambda text: analyzer.polarity_scores(text))
    sentiments_df = pd.DataFrame(sentiments.tolist())
    return pd.concat([df, sentiments_df], axis=1)