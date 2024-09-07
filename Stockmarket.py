
import streamlit as st
import yfinance as yf
import datetime
ticker_symbol = st.text_input("Enter Stock Name", "msft")

col1, col2, col3 = st.columns(3)

with col1:
    start_date = st.date_input("Start Date", datetime.date(2019, 7, 6))

with col2:
    end_date = st.date_input("End Date", datetime.date(2022, 7, 6))


data = yf.download(ticker_symbol, start=start_date, end= end_date)

st.write(data)

st.line_chart(data['Close'])

st.area_chart(data['Volume'])
