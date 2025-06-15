import streamlit as st
from stockData import stockAnalyze
import matplotlib.pyplot as plt

st.title("Stocks Trend Analyzer--Happy Father's Day!!")

ticker = st.text_input("Enter a stock ticker:", "AAPL")

if ticker:
    df = stockAnalyze(ticker)
    st.line_chart(df[["Close", "Moving Avg over 20 days", "Moving average over 50 days"]])