import streamlit as st
from stockData import stockAnalyze
import matplotlib.pyplot as plt

st.title("Stocks Trend Analyzer--Happy Father's Day!!")

ticker = st.text_input("Enter a stock ticker:", "AAPL").strip().upper()

if ticker:
    df = stockAnalyze(ticker)
    st.success(f"Data loaded for {ticker}")
    st.dataframe(df.tail()) 
    st.line_chart(df[["Close", "MA20", "MA50"]])

