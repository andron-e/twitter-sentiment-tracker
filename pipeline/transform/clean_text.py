import re
import pandas as pd

def clean_text(df):
    def preprocess(text):
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove links
        text = re.sub(r"@\w+|#\w+", "", text)                # Remove mentions/hashtags
        text = re.sub(r"[^a-zA-Z\s]", "", text)              # Keep only letters
        return text.lower().strip()

    # Only apply if 'text' column exists and is not empty
    if "text" in df.columns and not df.empty:
        df["text"] = df["text"].fillna("").apply(preprocess)
    else:
        print("Warning: No 'text' column found or DataFrame is empty in clean_text.")
    return df