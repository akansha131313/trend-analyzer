import yfinance as yf
import pandas as pd
import matplotlib.pyplot as ml

#stock analyzer method
def stockAnalyze(stocks):
    #gets the rolling avg for the close time
    ticker = yf.Ticker(stocks)
    df = ticker.history(period="6mo")
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    return df




