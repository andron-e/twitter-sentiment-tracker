from pipeline.transform import clean_text
import pandas as pd

def test_clean_text():
    df = pd.DataFrame({"content": ["This is GREAT!!! @elon https://t.co/x"]})
    cleaned = clean_text.clean_text(df)
    assert "great" in cleaned.iloc[0]["content"]