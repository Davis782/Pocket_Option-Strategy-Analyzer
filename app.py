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
from gsheetsdb import connect # Create a connection object.




# Create a Google Authentication connection object
# SERVICE_ACCOUNT_FILE = 'keys.json'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds =  service_account.Credentials.from_service_account_info( st.secrets["gcp_service_account"], scopes=["https://www.googleapis.com/auth/spreadsheets"] )
conn = connect(credentials=creds)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Ho6-7uRY3EuaPktr8a6uj9SshKyTaNNjI7uWg95nnfg'
service = build('sheets','v4',credentials=creds)
                
# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:Z9999").execute()

values = result.get('values', [])
print(values, 'These are the values')


aoa = [[ "1/1/2020",4000],["4/4/2020",3000],["7/12/2020",7000]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range= "Sheet3!B2", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
print(result, 'This is the result')

#
# if not values:
# 	print('No data found.')
# else:
# 	print('Name, Major:')
# 	for row in values:
# 		#Print columns A and E, which correspond to indices 0 and 4.
# 		print('%s, %s',  (row[0], row[4]))