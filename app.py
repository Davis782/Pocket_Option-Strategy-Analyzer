# Steamlet-Google Sheet
## Modules
# https://youtu.be/sO4IKex53JY?t=401   git add, git committ, git push example

import streamlit as st
from pandas import DataFrame
import pandas as pd
#for the spreadsheet information
# from gspread_pandas import Spread,Client
from google.oauth2 import service_account
from gsheetsdb import connect

st.set_page_config(layout="wide")


# Application Related Module
# import pubchempy as pcp

# from oauth2client.service_account import ServiceAccountCredentials

# Application Related Module
# Disable certificate verivication (Not necessary always)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Create a Google Authentication connection object
# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)





# scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
#
#
# # credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# credentials = service_account.Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"], scopes = scope)
# # client = gspread.authorize(credentials)
# client = Client(scope=scope,creds=credentials)
# spreadsheetname = 'Pocket-Option-df'
# spread = Spread(spreadsheetname,client = client)


# spreadsheet = client.open('Pocket-Option-df')

# New approach to connect to the GoogleSheet spreadsheet

@st.cache(allow_output_mutation=True)
# @st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows


# sheet_url= "https://docs.google.com/spreadsheets/d/1Ho6-7uRY3EuaPktr8a6uj9SshKyTaNNjI7uWg95nnfg/edit?usp=sharing"
# st.write(sheet_url)

sheet_url1 = st.secrets["private_gsheets_url"]
d = sheet_url1
st.write(d)
# sheet_url1=d["private_gsheets_url"]
st.write('private_gsheets_url' in d)
# True

# st.write(sheet_url1)
# st.write(d["private_gsheets_url"])
# sheet_url2=d["private_gsheets_url"]
# st.write(sheet_url2)

rows = run_query(f'SELECT * FROM "{d}"')


# Print results.
for row in rows:
    # st.write(f"{row} has a answer")

    df1 = pd.DataFrame(rows, columns=['TTT', 'Bbb', 'Cvv','dddd', 'BBBB', 'Cc','dcc', 'Bcc', 'Ccccc','dc', 'Bc', 'Cccccc','dcccc','ll','k'])


    # df = pd.concat([row, df], ignore_index=True)
st.write(df1,'I am here')
# print(df)

#Let's Check if the connectioin is established ?
# st.write(spread.url2)

# # Call our spreadsheet
# sh =client.open(spreadsheetname)
# worksheet_list = sh.worksheets()
# st.write(worksheet_list)


# Functions

# # Get our worksheets names
# def worksheet_names():
#     sheet_names = []
#     for sheet in worksheet_list:
#         sheet_names.append(sheet.title)
#     return sheet_names
#
# # Get the sheet as dataframe
# def load_the_spreadsheet(spreadsheetname):
#     worksheet = sh.worksheet(spreadsheetname)
#     df = DataFrame(worksheet.get_all_records())
#     return df
#
# # Update to Sheet
# def update_the_spreadsheet(spreadsheetname,dataframe):
#     col = ['Curreny Data','Time Info']
#     spread.df_to_sheet(dataframe[col],sheet=spreadsheetname,index=false)
#     st.sidebar.info("Updated to GoogleSheet")
#
#
#     # Check whether the sheets exists and throw the sheets to the users ?
#
#
#     # Throw the Currenincies to the Users so that they can access ?
#
#     # Load data from the Worksheets
# what_sheets = worksheet_names()
# #st.sidebar.write(what_sheets)
# ws_choice = st.sidebar.radio('Available worksheets', what_sheets)
#
#     # Create a Select box
# df = load_the_spreadsheet(ws_choice)
#
#     # Show the availability as selection
# select_Currency = st.sidebar.selectbox('Currency', list(df['Market_Name']))
#
#
# # def load_data1(df):
# #     # url = '/Users/Owner/PycharmProjects/Streamlit_Projects/Forex_Streamlit_App/Practice_Code/Data_Science_Apps/df1.csv'
# #     url = spread.url
# #     df = pd.read_csv(url, header = 0)
# #     return df
# # load_data1(df)
#
# # jj
# def load_data2(df):
#     load_the_spreadsheet(spreadsheetname)
#     # url = '/Users/Owner/PycharmProjects/Streamlit_Projects/Forex_Streamlit_App/Practice_Code/Data_Science_Apps/df2.csv'
#     # # url = spread.url
#     # df = pd.read_csv(url, header = 0)
#     return df
#
# print(load_data2(df))
#
# st.write(load_data2(df))




