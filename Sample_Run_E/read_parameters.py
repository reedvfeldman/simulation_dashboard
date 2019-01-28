#This file takes last row of spreadsheet as input
# reads parameters into key value pairs

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
row = ["E","CE2/run_E","36000","0","2.8e3","32","32","0","0","CE2","Leavitt","works!"]
sheet.insert_row(row, lastIndex+1)

#create key value pairs for parameters
parameters = sheet.row_values(1)
values_list = sheet.row_values(lastIndex)
params_dict = dict(zip(parameters, values_list))
print(params_dict)
