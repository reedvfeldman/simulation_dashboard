#This file takes last row of spreadsheet as input
# reads parameters into key value pairs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

# Extract and print all of the values
# row = ["E","CE2/run_E","36000","0","2.8e3","32","32","0","0","CE2","Leavitt","works!"]
# sheet.insert_row(row, lastIndex+1)

class Parameters():
    def __init__(self):
        self.status = 'incomplete'
        self.makeConnection()

    def makeConnection(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open("copy_busse_annulus_runs").sheet1
        return self.sheet

    def setParameters(self):
        lastIndex = len(self.sheet.get_all_values())
        values_list = self.sheet.row_values(lastIndex)
        self.identifier = values_list[0]
        self.configDirectory = values_list[1]
        self.rA = values_list[2]
        self.c = values_list[3]
        self.beta = values_list[4]
        self.nX = values_list[5]
        self.nY = values_list[6]
        self.Lambda = values_list[7]
        self.cuAmpl = values_list[8]
        self.type = values_list[9]
        self.machine = values_list[10]
        #run sim and update self.status to be in progress --> read parameter status

#create key value pairs for parameters
# parameters = sheet.row_values(1)

#params_dict = dict(zip(parameters, values_list))
#print(params_dict)

# output_file = open('slurm-1922.out', 'r').readlines()
# last = len(output_file)
# output = (output_file[last-5:last-1])
# print(output)
if __name__ == "__main__":
    spreadsheetParameters = Parameters()
    spreadsheetParameters.setParameters()
    print(spreadsheetParameters.__dict__)
