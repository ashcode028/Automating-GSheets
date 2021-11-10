
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive',]
# gc = pygsheets.authorize(service_file='client_secrets.json')
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client=gspread.authorize(creds)
