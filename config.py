# === config.py ===

# List of technical indicators to use as features
FEATURE_COLUMNS = [
    'SMA',
    'EMA',
    'RSI',
    'MACD',
    'OBV',
    'Momentum',
    'StdDev',
    'ROC',
    'Williams %R'
]

# The column name used for supervised target prediction
TARGET_COLUMN = 'Target'

# Default stock symbol if user does not provide one
DEFAULT_SYMBOL = 'TCS.NS'

# Train-test split ratio
TEST_SIZE = 0.2

# Random seed for reproducibility (optional)
RANDOM_STATE = 42
