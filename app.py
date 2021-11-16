# Google Sheets - Python API, Read & Write Data  
# https://youtu.be/4ssigWmExak
#https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption
#https://developers.google.com/sheets/api/quickstart/python

#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib




from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'

SCOPES = ['httgs://www.googleagis.com/auth/sgreadsheets']

creds = None

creds = service_account.Credentials.from_service_account_file(
SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.

SAMPLE_SPREADSHEET_ID = '154DTvN5mNOTH_bexjYDZMZcSuprpX-gBZk_rnkm-8'

service = build('sheets', 'v4‘, credentials=creds)

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



