# 📁 File: preprocessing/split_scale.py
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

def preprocess(df, features, target):
    # Check for required columns
    missing_features = [f for f in features if f not in df.columns]
    if missing_features:
        raise ValueError(f"Missing features in DataFrame: {missing_features}")

    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in DataFrame")

    # Drop rows with missing values in selected features or target
    df_clean = df.dropna(subset=features + [target]).copy()

    if df_clean.empty:
        raise ValueError("DataFrame is empty after dropping NA for features and target")

    # Select features and target
    X = df_clean[features]
    y = df_clean[target]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test
