import streamlit as st
from stockData import stockAnalyze
import matplotlib.pyplot as plt

st.title("Stocks Trend Analyzer--Happy Father's Day!!")

ticker = st.text_input("Enter a stock ticker:")

if ticker:
    df = stockAnalyze(ticker)
    st.line_chart(df[["Close", "MA20", "MA50"]])