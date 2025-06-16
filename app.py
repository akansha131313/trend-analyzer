import streamlit as st
from stockData import stockAnalyze
import matplotlib.pyplot as plt

st.title("Stocks Trend Analyzer")

ticker = st.text_input("Enter a stock ticker:", "AAPL")

if ticker:
    df = stockAnalyze(ticker)
    if df is None or df.empty:
        st.error("No data found. Please check the ticker symbol or try again later.")
    else:
        st.success(f"Data loaded for {ticker}")
        st.subheader("Historical Data (Last 5 rows)")
        st.dataframe(df.tail())
        st.line_chart(df[["Close", "MA20", "MA50"]])
