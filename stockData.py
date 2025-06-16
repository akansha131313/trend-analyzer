import yfinance as yf
import pandas as pd
import matplotlib.pyplot as ml

#stock analyzer method
def stockAnalyze(stocks):
    #gets the rolling avg for the close time
    for stock in stocks:
        ticker = yf.Ticker(stock)
        df = ticker.history(period="6mo")
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        df[['Close', 'MA20', 'MA50']].plot(figsize=(10,6), title="Moving Average Trend of ")
        ml.grid(True)
        ml.show()
        return df




