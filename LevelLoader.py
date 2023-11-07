import json

def LoadLevelsFromJson():
    with open("levels_data.json","r") as MyFile:
        data = json.load(MyFile)
        return data