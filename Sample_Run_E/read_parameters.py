#This file takes last row of spreadsheet as input
# reads parameters into key value pairs
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import configparser
from pathlib import Path


class Parameters():
    idCounter = 0
    stop = False
    def __init__(self):
        Parameters.idCounter += 1
        self.name = 'Parameters_{0}'.format(Parameters.idCounter)
        self.status = 'incomplete'
        self.sheet = self.makeConnection()
        self.lastIndex = len(self.sheet.get_all_values())
        self.setParameters()
        self.readConfig()
        self.createConfig()
        self.createDirectory()

    def makeConnection(self):
        print('making connection')
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('/home/rfeldman/simulation_dashboard/Sample_Run_E/client_secret.json', scope)
        client = gspread.authorize(creds)
        return client.open("copy_busse_annulus_runs").sheet1

    def getLastIndex(self):
        return len(self.makeConnection().get_all_values())

    #write functionality that doesn't break if someone doesn't have enough params
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

    #readConfig takes the global .cfg file as input
    def readConfig(self):
        print('readingConfig')
        config = configparser.ConfigParser()
        config.read('example.cfg')
        self.buildLocation = config['Paths']['base_dir'] + str(self.identifier)
        print(self.buildLocation)

    #createConfig will create the local config file inside the project directory
    #Must read global config first so that you know where to put local one
    #this function should be called by createDirectory()
    def createConfig(self):
        print('creatingLocal conig')
        self.config = configparser.ConfigParser()
        self.config['DEFAULT'] = {'ID': self.name,
                             'Identifier': self.identifier,
                             'Machine': self.machine
                             }
        #place location corresponding to Levitt folder structure
        self.config['Location'] = {'Directory': self.buildLocation,
                              'ConfigFile': self.buildLocation + '/' + str(self.identifier + '.cfg')}
        return self.config

    #use pathlib to create directory
    #take example config as input
    def createDirectory(self):
        print('creatingDirectory')
        run_dir = Path.home().joinpath(self.buildLocation)
        print(Path.home() / (self.buildLocation))
        run_dir.mkdir(exist_ok=True, parents=True)
        configFile = run_dir.joinpath('run_' + str(self.identifier) + '.cfg')
        with configFile.open('w') as wf:
            self.config.write(wf)
        runFile = run_dir.joinpath('run_' + str(self.identifier) + '_kturb.sh')
        simFile = run_dir.joinpath('kturb.py')
        #maybe have fileList read from global config??
        fileList = [runFile, simFile]
        for item in fileList:
            with item.open("w") as f:
                f.write('Your Code Goes Here')
        with runFile.open('w') as rf:
            rf.write('Hello World!')    
#create key value pairs for parameters
#parameters = sheet.row_values(1)
#params_dict = dict(zip(parameters, values_list))
# lastIndex = len(self.sheet.get_all_values())
# values_list = self.sheet.row_values(lastIndex)
#print(params_dict)
