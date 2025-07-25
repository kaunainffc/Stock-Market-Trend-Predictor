import yfinance as yf
def load_data(symbol):
    df = yf.download(symbol, start="2013-01-01")
    df.reset_index(inplace=True)
    return df
