import streamlit as st
from stockData import stockAnalyze
import matplotlib.pyplot as plt

st.title("Stocks Trend Analyzer--Happy Father's Day!!")

ticker = input("Enter a stock ticker:")
data = st.text_input("Enter a stock ticker:", ticker )

if data:
    st.line_chart(stockAnalyze(data))