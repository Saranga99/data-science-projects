import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""# Simple Stock Price App

google stock closing price and volume of Google""")


# define the ticker symble
tickerSymbol = "GOOGL"

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get historical prices for this ticker
tickerDf = tickerData.history(period="1d", start="2010-5-26", end="2021-5-26")

# open high low close volume dividends stock spilts
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
