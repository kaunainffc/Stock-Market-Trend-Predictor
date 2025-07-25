import sys
import os
# 📁 File: main.py
import yfinance as yf
import pandas as pd
from features.indicators import add_indicators
from features.labels import create_labels
from preprocessing.split_scale import preprocess
from models.train import train_models
from models.ensemble import vote
from config import FEATURE_COLUMNS, TARGET_COLUMN

def run_pipeline(symbol):
    df = yf.download(symbol, period="3mo")

    # Flatten columns if MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.map(lambda x: x[0])

    print("📊 Available columns in DF:", df.columns.tolist())

    if df.empty or len(df) < 30:
        print("❌ Not enough data")
        return None, df

    # Add indicators
    df = add_indicators(df)

    # Create labels
    df = create_labels(df)
    if 'Target' not in df.columns:
        print("❌ Target column not found. Cannot proceed.")
        return None, df

    # Preprocessing
    try:
        X_train, X_test, y_train, y_test = preprocess(
            df, features=FEATURE_COLUMNS, target='Target')
    except Exception as e:
        print("❌ Preprocessing failed:", e)
        return None, df

    # Train and predict
    models = train_models(X_train, y_train)
    prediction = vote(models, X_test)

    return prediction, df