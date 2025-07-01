import re
import pandas as pd

def clean_text(df):
    def preprocess(text):
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove links
        text = re.sub(r"@\w+|#\w+", "", text)                # Remove mentions/hashtags
        text = re.sub(r"[^a-zA-Z\s]", "", text)              # Keep only letters
        return text.lower().strip()

    df["content"] = df["content"].apply(preprocess)
    return df