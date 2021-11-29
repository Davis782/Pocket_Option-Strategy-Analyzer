# Google Sheets - Python API, Read & Write Data
# https://youtu.be/4ssigWmExak
#https://developers.google.com/identity/protocols/oauth2/service-account#python
#https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption
#https://developers.google.com/sheets/api/quickstart/python

#   pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


import streamlit as st
import pandas as pd
# import schedule
# import time
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2 import service_account
from gsheetsdb import connect # Create a connection object.

st.set_page_config(layout="wide")


# Create a Google Authentication connection object
# SERVICE_ACCOUNT_FILE = 'keys.json'
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]



creds = None
creds =  service_account.Credentials.from_service_account_info( st.secrets["gcp_service_account"], scopes=scope )
conn = connect(credentials=creds)


# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID=st.secrets["SAMPLE_SPREADSHEET_ID"]["SAMPLE_SPREADSHEET_ID"]
service = build('sheets','v4',credentials=creds)




st.title('Welcome to the Pocket Options Trading Analyzer')

st.markdown("""
This app retrieves the Currency Pair data and runs it against numerous Strategies.  The results of passing the Strategies shows up in the tables below!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Pocket Option](https://PocketOption.com).
* **Suggestions:** Right Click above link and place in a new window, Open up a few Trading Currencies of interest and setup for Trading
""")

st.sidebar.header('User Input Features')

def Pocket_Option(x):

    # Call the Sheets API
    sheet = service.spreadsheets()
    result1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="df1!A1:O22").execute()

    values1 = result1.get('values', [])
    #print(values1, 'These are the values')
    # st.write(values)

    df1 = pd.DataFrame.from_records(values1)
    st.header('Display Currencies in Selected Sector Going Up')
    st.write(df1)

    # Call the Sheets API
    sheet2 = service.spreadsheets()
    result2 = sheet2.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="df2!A1:O22").execute()

    values2 = result2.get('values', [])
    #print(values1, 'These are the values')
    # st.write(values)

    df2 = pd.DataFrame.from_records(values2)
    st.header('Display Currencies in Selected Sector Going Down')
    st.write(df2)


# schedule.every(500).seconds.do(New_Data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# HtmlFile = open(“<script src="https://cdn.logwork.com/widget/text.js"></script>
# <a href="https://logwork.com/current-time-in-kerrville-united-states-texas" class="clock-widget-text" data-timezone="America/Chicago" data-language="en">Kerrville, United States</a>”, ‘r’, encoding=‘utf-8’)
# source_code_2 = HtmlFile.read()
# components.html(source_code_2, height=700)

for x in range(1000):
  Pocket_Option(x)
#   time.sleep(1)

