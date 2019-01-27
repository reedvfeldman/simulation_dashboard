import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("copy_busse_annulus_runs").sheet1
lastIndex = len(sheet.get_all_values())
# Extract and print all of the values
row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python","this","is","a","test"]
sheet.insert_row(row, lastIndex+1)
