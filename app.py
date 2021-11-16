# Google Sheets - Python API, Read & Write Data  
# https://youtu.be/4ssigWmExak
#https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption
#https://developers.google.com/sheets/api/quickstart/python

#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


import streamlit as st
import pandas as pd

from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'

SCOPES = ['httgs://www.googleagis.com/auth/sgreadsheets']

creds = None

creds = service_account.Credentials.from_service_account_file(
SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.

SAMPLE_SPREADSHEET_ID = '154DTvN5mNOTH_bexjYDZMZcSuprpX-gBZk_rnkm-8'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
range="sales!A1:G16").execute()

values = result.get('values', [])
aoa = [[ "1/1/2020",4000],["4/4/2020",3000],["7/12/2020",7000]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
range= "Sheet2!B2", valueInputOption="USER_ENTERED", body={ "values":aoa}).execute()
print(request)

if not values:
	print('No data found.')
else:
	print('Name, Major:')
	for row in values:
		#Print columns A and E, which correspond to indices 0 and 4.
		print('%s, %s'  (row[0], row[4]))

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



