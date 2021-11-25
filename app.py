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
from google.oauth2 import service_account
from gsheetsdb import connect # Create a connection object.


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


# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet3!A1:O22").execute()

values = result.get('values', [])
#print(values1, 'These are the values')
# st.write(values)

df1 = pd.DataFrame.from_records(values)
st.write(df1)


# # Call the Sheets API
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Sheet3!A1:O22").execute()

# values = result.get('values', [])
# print(values, 'These are the values')
# st.write(values)


# aoa = values 
# request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                 range= "Sheet4!B2", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
# st.write(request)

# df1 = pd.DataFrame.from_records(request)
# st.write(df1)


#
# if not values:
# 	print('No data found.')
# else:
# 	print('Name, Major:')
# 	for row in values:
# 		#Print columns A and E, which correspond to indices 0 and 4.
# 		print('%s, %s',  (row[0], row[4]))
