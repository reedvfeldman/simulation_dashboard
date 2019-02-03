from read_parameters import Parameters
import time

def readDataFeed():
    print('readDataFeed function started')
    runs = []
    last = len(runs)-1
    spreadsheetParameters = Parameters()
    runs.append(spreadsheetParameters)
    print('while loop')
    while not spreadsheetParameters.stop:
        print('last run in list:')
        print(runs[last].__dict__)
        time.sleep(30)
        print(spreadsheetParameters.lastIndex)
        print(spreadsheetParameters.getLastIndex())
        if spreadsheetParameters.lastIndex < spreadsheetParameters.getLastIndex():
            print('new row added')
            spreadsheetParameters = Parameters()
            runs.append(spreadsheetParameters)
        else:
            print('nothing has changed')
            continue

readDataFeed()
