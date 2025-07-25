# 📁 File: features/labels.py

def create_labels(df):
    """
    Creates a binary target column 'Target':
    - 1 if next day's Close is higher than current day
    - 0 otherwise
    """
    if 'Close' not in df.columns:
        raise ValueError("'Close' column not found for label generation.")

    df = df.copy()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

    print("✅ Label column 'Target' created successfully.")
    return df
