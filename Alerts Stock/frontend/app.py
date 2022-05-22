from os import name
from matplotlib.pyplot import title
import streamlit as st
import requests
import json
import sys
import time
import pandas as pd
import altair as alt

# page_bg_img = '''
# <style>
# body {
# background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

add_data_url = 'http://127.0.0.1:8000/add_data/'
get_data_url = 'http://127.0.0.1:8000/get_data'
get_trigger_url = 'http://127.0.0.1:8000/db-alerts-stocks'

st.set_page_config(page_title="Alerts Stock",layout="wide",
     initial_sidebar_state="expanded",)

st.title("Alerts Stock")

st.sidebar.image("https://miro.medium.com/max/1000/1*B_R11J_9G4U3lac0omktLQ.png", width=100,
                 channels='BGR', output_format='PNG')

def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}
session = requests.Session()
# st.sidebar.header("Alerts Stock")
# with st.sidebar.expander("Info"):
#     st.info(f"""
#         Click [here](https://finance.yahoo.com/cryptocurrencies/)
#         for a list of cryptocurrencies symbols on Yahoo Finance.
#         """)


col1, col2 = st.sidebar.columns([1,1])

with col1:
    add_stock_btn = st.button("Add stock")
with col2:
    rem_stock_btn = st.button("Remove stock")

if rem_stock_btn:
    st.sidebar.subheader("Add new stock...")
    name_of_stock = st.sidebar.text_input("Enter name of the stock")
    if st.sidebar.button('Remove'):
        rem_stock_btn = True
        st.sidebar.write('Stock removed')
        time.sleep(3)
        rem_stock_btn = False


else:
    st.sidebar.subheader("Add new stock...")
    name_of_stock = st.sidebar.text_input("Enter name of the stock")
    trend = st.sidebar.radio("Select the Trend: ", ('Up Trend', 'Down Trend'))
    price_trigger = st.sidebar.text_input("Enter the price trigger")

    if st.sidebar.button('Submit'):
        if name_of_stock == None or trend == None or price_trigger == None:
            st.sidebar.error('Please input all the fields!')
        else:
            if trend == 'Up Trend':
                up_trend = True
            else: up_trend = False
            data = {
                "stock_name":name_of_stock,
                "up_trends":up_trend, 
                "price_trigger":float(price_trigger)
            }
            # print(json.dumps(data))
            response = requests.post(add_data_url, data = json.dumps(data))

            if response:
                placeholder = st.empty()
                # with st.sidebar.empty():
                sta = st.sidebar.write(f"⏳ Data is submitting")
                time.sleep(3)

                st.sidebar.success("✔️ ' Stock added succesfully!")
                placeholder.empty()
                

    else:
        st.sidebar.write('')

stock_data = fetch(session, get_data_url)



df = pd.json_normalize(stock_data) 
df['price_trigger'].round(2)
df.rename(columns = {'stock_name':'Name of the stoks', 'up_trends':'Trend', 'price_trigger': 'Price Trigger'}, inplace = True)
df["Trend"].replace({True: 'Up trend', False: 'Down trend'}, inplace=True)
df['Price Trigger'] = df['Price Trigger'].round(2)
styler = df.style.hide_index()

st.write(styler.to_html(), unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
col1, col2 = st.columns([1,1])

with col1:
    st.write("See what's in trigger...")
with col2:
    refresh = st.button('Refresh')

if refresh:
    trigger = fetch(session, get_trigger_url)
    print (trigger)
    trigger_df = pd.json_normalize(trigger)
    for x, y in trigger.items():
        message = x + y 
        st.info(message)
