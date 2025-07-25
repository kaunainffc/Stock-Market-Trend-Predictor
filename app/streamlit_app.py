import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# 📁 File: app/streamlit_app.py
import streamlit as st
from app.db import init_db, validate_user, add_user, get_watchlist, add_to_watchlist, plot_stock_price
from main import run_pipeline

# Initialize database
init_db()

# ------------------------
# 🧠 Sidebar: Login / Register
# ------------------------
st.sidebar.title("🔐 User Authentication")
auth_mode = st.sidebar.radio("Choose Option", ["Login", "Register"])
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if auth_mode == "Register":
    if st.sidebar.button("Create Account"):
        add_user(username, password)
        st.sidebar.success("✅ Account created! Please login.")

if auth_mode == "Login":
    if st.sidebar.button("Login"):
        if validate_user(username, password):
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.sidebar.success(f"✅ Welcome, {username}!")
        else:
            st.sidebar.error("❌ Invalid credentials")

# ------------------------
# 🚫 Stop app if not logged in
# ------------------------
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please login to use the app.")
    st.stop()

# ------------------------
# 🧠 Main App
# ------------------------
st.title("📈 Stock Market Trend Predictor")
symbol = st.text_input("Enter stock symbol (e.g., TCS.NS):")

if symbol:
    st.write("🔍 Fetching & Predicting...")
    prediction, df = run_pipeline(symbol)

    if prediction is None:
        st.error("❌ Prediction failed: Not enough data or invalid symbol.")
    else:
        if prediction == 1:
            result_text = "📈 Increase"
        elif prediction == 0:
            result_text = "📉 Decrease"
        else:
            result_text = f"⚠️ Unknown output: {prediction}"

        st.success(f"Prediction for {symbol}: {result_text}")

        # ✅ Add to watchlist
        if st.button("⭐ Add to Watchlist"):
            add_to_watchlist(st.session_state["user"], symbol)
            st.success(f"Added {symbol} to your watchlist.")

        # ✅ Plot
        st.subheader("📊 Stock Price Trend (Last 30 Days)")
        plot_stock_price(symbol)

# ------------------------
# 📜 Watchlist Section
# ------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("👁️‍🗨️ Your Watchlist")
user_watchlist = get_watchlist(st.session_state["user"])

if user_watchlist:
    st.sidebar.write("\n".join(user_watchlist))
else:
    st.sidebar.write("🔎 No stocks in watchlist yet.")
