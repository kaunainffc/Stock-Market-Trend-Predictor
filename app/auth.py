import streamlit as st
from app.db import add_user, validate_user

def login_ui():
    st.sidebar.title("🔐 Login / Register")

    auth_choice = st.sidebar.radio("Login or Register?", ("Login", "Register"))
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if auth_choice == "Register":
        if st.sidebar.button("Create Account"):
            add_user(username, password)
            st.success("✅ Account created! Now login.")

    if auth_choice == "Login":
        if st.sidebar.button("Login"):
            if validate_user(username, password):
                st.session_state.user = username
                st.success(f"✅ Welcome {username}!")
            else:
                st.error("❌ Invalid credentials")
