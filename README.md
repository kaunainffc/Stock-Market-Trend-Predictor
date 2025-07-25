# 📈 Stock Market Trend Prediction App
A web-based ML-powered application built with **Streamlit** to predict stock trends (up or down) using historical data, technical indicators, and ensemble learning models.
## 🚀 Features

- ✅ Predict stock price movement (↑/↓) using ML models
- 📊 Technical Indicators: SMA, EMA, RSI, MACD, OBV, Momentum, ROC, etc.
- 🧠 Ensemble modeling with voting
- 🔒 User Login System (SQLite or MongoDB)
- 🕵️ Track who logged in and when (login activity logging)
- 📉 Interactive graphs and predictions
- 🌐 Deployable on Streamlit Cloud / Render / Hugging Face

---

## 🗂️ Project Structure

Stock-Trend-App/
├── app/
│ ├── streamlit_app.py # Main Streamlit interface
│ ├── db.py # DB connection (SQLite/MongoDB)
│ └── auth.py # Login, Register, Session
│
├── features/
│ ├── indicators.py # Add technical indicators
│ └── labels.py # Create binary labels (up/down)
│
├── models/
│ ├── train.py # Train base models
│ └── ensemble.py # Voting ensemble logic
│
├── preprocessing/
│ └── split_scale.py # Preprocess: scale + split
│
├── config.py # Configurable constants
├── main.py # Pipeline runner
├── requirements.txt # Required packages
└── README.md # You're here!

yaml
Copy
Edit

---

## 🧠 ML Models Used

- **Random Forest**
- **Logistic Regression**
- **Gradient Boosting**
- **Voting Classifier** for final decision

---

## ⚙️ How It Works

1. User enters a stock ticker symbol (e.g. `TCS.NS`)
2. App fetches 3-month historical data via `yfinance`
3. Adds technical indicators
4. Creates a binary target (`1 = increase`, `0 = decrease`)
5. Preprocesses data, scales features
6. Trains models and combines predictions using ensemble voting
7. Displays the predicted trend and graph 📈

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/stock-trend-app.git
cd stock-trend-app

# 2. (Optional) Create virtual env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app/streamlit_app.py
🔗 Tech Stack

	Python
	Streamlit
scikit-learn, pandas
Data	yfinance
SQLite / MongoDb
Streamlit Cloud / Render
