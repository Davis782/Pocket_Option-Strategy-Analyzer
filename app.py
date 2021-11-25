# Google Sheets - Python API, Read & Write Data
# https://youtu.be/4ssigWmExak
#https://developers.google.com/identity/protocols/oauth2/service-account#python
#https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption
#https://developers.google.com/sheets/api/quickstart/python

#   pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account




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
                
