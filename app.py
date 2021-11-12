
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf


import os, ssl
#
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
#         getattr(ssl, '_create_unverified_context', None)):
ssl._create_default_https_context = ssl._create_unverified_context
#
# #  http://localhost:5997

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")


#===========================Update=================================================
# Create a Google Authentication connection object
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


# credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes = scope)
# client = gspread.authorize(credentials)
client = Client(scope=scope,creds=credentials)
spreadsheetname = 'Pocket-Option-df'
spread = Spread(spreadsheetname,client = client)
#============================================================================

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

#Let's Check if the connectioin is established ?
#st.write(spread.url)

# Call our spreadsheet
sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()
st.write(worksheet_list)


# Functions

# Get our worksheets names
def worksheet_names():
    sheet_names = []
    for sheet in worksheet_list:
        sheet_names.append(sheet.title)
    return sheet_names

# Get the sheet as dataframe
def load_the_spreadsheet(spreadsheetname):
    worksheet = sh.worksheet(spreadsheetname)
    df = DataFrame(worksheet.get_all_records())
    return df

# Update to Sheet
def update_the_spreadsheet(spreadsheetname,dataframe):
    col = ['Curreny Data','Time Info']
    spread.df_to_sheet(dataframe[col],sheet=spreadsheetname,index=false)
    st.sidebar.info("Updated to GoogleSheet")


    # Check whether the sheets exists and throw the sheets to the users ?


    # Throw the Currenincies to the Users so that they can access ?

    # Load data from the Worksheets
what_sheets = worksheet_names()
#st.sidebar.write(what_sheets)
ws_choice = st.sidebar.radio('Available worksheets', what_sheets)

    # Create a Select box
df = load_the_spreadsheet(ws_choice)

    # Show the availability as selection
select_Currency = st.sidebar.selectbox('Currency', list(df['Market_Name']))


# def load_data1(df):
#     # url = '/Users/Owner/PycharmProjects/Streamlit_Projects/Forex_Streamlit_App/Practice_Code/Data_Science_Apps/df1.csv'
#     url = spread.url
#     df = pd.read_csv(url, header = 0)
#     return df
# load_data1(df)

# jj
def load_data2(df):
    load_the_spreadsheet(spreadsheetname)
    # url = '/Users/Owner/PycharmProjects/Streamlit_Projects/Forex_Streamlit_App/Practice_Code/Data_Science_Apps/df2.csv'
    # # url = spread.url
    # df = pd.read_csv(url, header = 0)
    return df

print(load_data2(df))

st.write(load_data2(df))




