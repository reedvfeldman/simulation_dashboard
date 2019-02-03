#This file takes last row of spreadsheet as input
# reads parameters into key value pairs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Parameters():
    idCounter = 0
    stop = False
    def __init__(self):
        Parameters.idCounter += 1
        self.name = 'Parameters_{0}'.format(Parameters.idCounter)
        self.status = 'incomplete'
        self.sheet = self.makeConnection()
        self.lastIndex = self.getLastIndex()
        self.setParameters()

    def makeConnection(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        return client.open("copy_busse_annulus_runs").sheet1

    def getLastIndex(self):
        return len(self.makeConnection().get_all_values())

    def setParameters(self):
        values_list = self.sheet.row_values(self.lastIndex)
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
#parameters = sheet.row_values(1)
#params_dict = dict(zip(parameters, values_list))
# lastIndex = len(self.sheet.get_all_values())
# values_list = self.sheet.row_values(lastIndex)
#print(params_dict)
