# 📁 File: app/db.py
import sqlite3
import os

# 📁 File: app/db.py
import sqlite3
import os
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

# ✅ Absolute DB path inside data/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "data", "watchlist.db")


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS watchlists (
            username TEXT,
            symbol TEXT,
            PRIMARY KEY (username, symbol)
        )
    """)
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def validate_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    return row and row[0] == password


def get_watchlist(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT symbol FROM watchlists WHERE username=?", (username,))
    results = c.fetchall()
    conn.close()
    return [r[0] for r in results]


def add_to_watchlist(username, symbol):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO watchlists (username, symbol) VALUES (?, ?)", (username, symbol))
    conn.commit()
    conn.close()


def plot_stock_price(symbol):
    data = yf.download(symbol, period="1mo")
    if data.empty:
        st.warning("No data available to plot.")
        return

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(data.index, data['Close'], label="Close Price", color="blue")
    ax.set_title(f"Last 30 Days Price Trend: {symbol}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)
