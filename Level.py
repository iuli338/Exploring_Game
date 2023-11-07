from LevelLoader import LoadLevelsFromJson

class Level:

    allLevels = []

    def __init__(self,nume:str,text:str,alegeriTextList:list,eventsDict:dict):
        self.nume = nume
        self.text = text
        self.alegeriTextList = alegeriTextList
        self.eventsDict = eventsDict
        #
        Level.allLevels.append(self)

    def CreateLevels():
        data = LoadLevelsFromJson()
        for level in data:
            newLevel = Level (level["nume"],level["text"],level["alegeriTextList"],level["eventsDict"])
