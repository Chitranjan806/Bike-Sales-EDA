import yfinance as yf
import streamlit as st
import pandas as pandas

st.write("""
    # Simple stock price App
    Shown are the stock closing price of Google
              
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

ticker_df = tickerData.history(period='1d', start='2010-01-01', end='2024-08-31')
# Open  High    Low Close   Volume  Dividends   Stock Splits

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)