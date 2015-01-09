import json

def saveJSON(filename,data):
    "saves the data object as a JSON string"
    with open(filename,"w") as openFile:
        openFile.write(json.dumps(data))