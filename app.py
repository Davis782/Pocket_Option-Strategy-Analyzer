
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf


# import os, ssl
#
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
#         getattr(ssl, '_create_unverified_context', None)):
#     ssl._create_default_https_context = ssl._create_unverified_context
#
# #  http://localhost:5997

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.title('Welcome to the Pocket Options Trading Analyzer')

st.markdown("""
This app retrieves the Currency Pair data and runs it against numerous Strategies.  The results of passing the Strategies shows up in the tables below!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Pocket Option](https://PocketOption.com).
* **Suggestions:** Right Click above link and place in a new window, Open up a few Trading Currencies of interest and setup for Trading
""")

st.sidebar.header('User Input Features')

# Web scraping of S&P 500 data
#
@st.cache
def load_data1():
    url = '/Users/Owner/PycharmProjects/Streamlit_Projects/Forex_Streamlit_App/Practice_Code/Data_Science_Apps/df1.csv'
    df1 = pd.read_csv(url, header = 0)
    return df1

def load_data2():
    url = '/Users/Owner/PycharmProjects/Streamlit_Projects/Forex_Streamlit_App/Practice_Code/Data_Science_Apps/df2.csv'
    df2 = pd.read_csv(url, header = 0)
    return df2




df1 = load_data1()
df2 = load_data2()


df1.reset_index()
df2.reset_index()


sector1 = df1.groupby('Market_Name')
sector2 = df2.groupby('Market_Name')


# Sidebar - Sector selection
sorted_sector_unique1 = sorted( df1['Market_Name'].unique() )
selected_sector1 = st.sidebar.multiselect('Market_Name', sorted_sector_unique1, sorted_sector_unique1, key = "test1")

sorted_sector_unique2 = sorted( df2['Market_Name'].unique() )
selected_sector2 = st.sidebar.multiselect('Market_Name', sorted_sector_unique2, sorted_sector_unique2, key = "test2")

# Filtering data
df_selected_sector1 = df1[ (df1['Market_Name'].isin(selected_sector1)) ]
df_selected_sector2 = df2[ (df2['Market_Name'].isin(selected_sector2)) ]



st.header('Display Currencies in Selected Sector Going Down')
st.write('Data Dimension: ' + str(df_selected_sector1.shape[0]) + ' rows and ' + str(df_selected_sector1.shape[1]) + ' columns.')
st.dataframe(df_selected_sector1)


st.header('Display Currencies in Selected Sector Going Up')
st.write('Data Dimension: ' + str(df_selected_sector2.shape[0]) + ' rows and ' + str(df_selected_sector2.shape[1]) + ' columns.')
st.dataframe(df_selected_sector2)
