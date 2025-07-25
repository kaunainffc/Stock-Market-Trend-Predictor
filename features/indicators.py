def add_indicators(df):
    import numpy as np
    import pandas as pd

    df = df.reset_index(drop=True)  # Ensure simple index

    # --- SMA & EMA
    df['SMA'] = df['Close'].rolling(window=14).mean()
    df['EMA'] = df['Close'].ewm(span=14).mean()

    # --- RSI
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # --- MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2

    # ✅ OBV using NumPy vectorization (final fix)
    close_diff = df['Close'].diff()
    direction = np.sign(close_diff.fillna(0))
    obv = (direction * df['Volume']).fillna(0).cumsum()
    df['OBV'] = obv

    # --- Momentum
    df['Momentum'] = df['Close'] - df['Close'].shift(10)

    # --- StdDev
    df['StdDev'] = df['Close'].rolling(10).std()

    # --- ROC
    df['ROC'] = df['Close'].pct_change(periods=10)

    # --- Williams %R
    high_14 = df['High'].rolling(14).max()
    low_14 = df['Low'].rolling(14).min()
    df['Williams %R'] = (high_14 - df['Close']) / (high_14 - low_14) * -100

    df = df.dropna()
    return df
