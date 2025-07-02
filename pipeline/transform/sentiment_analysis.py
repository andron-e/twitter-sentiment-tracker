from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
labels = ['negative', 'neutral', 'positive']

def apply(df):
    sentiments = []
    # Use 'text' column if available, fallback to 'content' for legacy support
    text_col = 'text' if 'text' in df.columns else ('content' if 'content' in df.columns else None)
    if text_col is None or df.empty:
        print("Warning: No 'text' or 'content' column found or DataFrame is empty in sentiment_analysis.")
        df["sentiment"] = []
        return df
    for text in df[text_col]:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        sentiment_idx = torch.argmax(probs).item()
        sentiments.append(labels[sentiment_idx])
    df["sentiment"] = sentiments
    return df