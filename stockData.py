import yfinance as yf
import pandas as pd

#stock analyzer method
def stockAnalyze(name):
    #gets the rolling avg for the close time
    ticker = yf.Ticker(name)
    df = ticker.history(period="6mo")
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    return df


