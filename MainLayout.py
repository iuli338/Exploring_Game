import pygame
from Button import Button
from Level import Level
import Inventar

class MainLayout:

    levelName = None
    levelImageRect = None
    levelImage = None
    levelText = None
    levelEvents = None
    livesImage = None

    layoutXCord = 100

    TextFont = None
    TextColor = pygame.Color(255,255,255)

    buttons = []
    
    @staticmethod
    def Init(screen):

        # Initing the fost
        pygame.font.init()
        MainLayout.TextFont = pygame.font.Font(None, 28)

        # Initing the image
        imageSize = (800,450)
        screenSize = screen.get_size()
        imagePosition = [screenSize[0]//2-imageSize[0]//2,MainLayout.layoutXCord]
        MainLayout.levelImageRect = pygame.Rect(imagePosition,imageSize)
        # "image0.png" is the placeholder white image
        MainLayout.locationImageIMG = pygame.image.load("res/image0.png")

        # Initing the locationName and locationText
        MainLayout.levelName = MainLayout.TextFont.render("Location name:", True, MainLayout.TextColor)
        MainLayout.levelText = MainLayout.TextFont.render("Text text text...", True, MainLayout.TextColor)

        # Initing the buttons
        ButtonPos = [MainLayout.levelImageRect.x,MainLayout.levelImageRect.y+MainLayout.levelImageRect.height+42]
        MainLayout.buttons.append(Button(ButtonPos,"Alegere 1"))
        ButtonPos[1] += 40
        MainLayout.buttons.append(Button(ButtonPos,"Alegere 2"))
        ButtonPos[1] += 40
        MainLayout.buttons.append(Button(ButtonPos,"Alegere 3"))

    def Draw(screen):
        # locationImage
        pygame.draw.rect(screen, MainLayout.TextColor, MainLayout.levelImageRect)
        screen.blit(MainLayout.levelImage,MainLayout.levelImageRect.topleft)
        # locationName
        locationNamePos = [MainLayout.levelImageRect.x,MainLayout.levelImageRect.y-28]
        screen.blit(MainLayout.levelName,locationNamePos)
        # locationText
        locationTextPos = [MainLayout.levelImageRect.x,MainLayout.levelImageRect.y+MainLayout.levelImageRect.height+10]
        screen.blit(MainLayout.levelText,locationTextPos)

    def HandleLoadedLevelEvents(levelToHandle):
        if levelToHandle.eventsDict == None:
            return
        if "ChangeImageOnStart" in levelToHandle.eventsDict:
            newImagePath = levelToHandle.eventsDict["ChangeImageOnStart"]
            MainLayout.levelImage = pygame.image.load(newImagePath)

    def TryLoadLevel(nume):
        for level in Level.allLevels:
            if level.nume == nume:
                MainLayout.LoadLevel(level)
                return
        print("Nu a fost gasit un nivel cu asa nume.")

    def LoadLevel(levelToLoad):
        # Initing the locationName and locationText
        MainLayout.levelName = MainLayout.TextFont.render(levelToLoad.nume, True, MainLayout.TextColor)
        MainLayout.levelText = MainLayout.TextFont.render(levelToLoad.text, True, MainLayout.TextColor)
        MainLayout.levelEvents = levelToLoad.eventsDict
        for i in range (0,3):
            if levelToLoad.alegeriTextList[i] != None:
                MainLayout.buttons[i].ChangeText(levelToLoad.alegeriTextList[i])
                MainLayout.buttons[i].SetDisabled(False)
            else:
                MainLayout.buttons[i].ChangeText("- - -")
                MainLayout.buttons[i].SetDisabled(True)
            #
            if "DisabledButtonIndexes" in MainLayout.levelEvents:
                for i in range (0,3):
                    if i in MainLayout.levelEvents["DisabledButtonIndexes"]:
                        MainLayout.buttons[i].SetDisabled(True)
            #
        MainLayout.HandleLoadedLevelEvents(levelToLoad)

    def ChangeLevelImage(newImagePath):
        MainLayout.levelEvents["ChangeImageOnStart"] = newImagePath
        MainLayout.levelImage = pygame.image.load(newImagePath)

    def HandleButtonsClick(event,mouseX,mouseY):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clickedButtonIndex = None
            for i in range(0,3):
                if MainLayout.buttons[i].rect.collidepoint(mouseX,mouseY):
                    clickedButtonIndex = i
                    break
            if clickedButtonIndex == None:
                return

            ## ChangeImageOnClick
            if "ChangeImageOnClick" in MainLayout.levelEvents:
                if MainLayout.levelEvents["ChangeImageOnClick"]["buttonIndex"] == clickedButtonIndex:
                    # Check if it requires an item
                    if "RequiresItem" in MainLayout.levelEvents["ChangeImageOnClick"]:
                        if Inventar.itemsDict[MainLayout.levelEvents["ChangeImageOnClick"]["RequiresItem"]["ItemName"]] == 0:
                            failText = MainLayout.levelEvents["ChangeImageOnClick"]["RequiresItem"]["FailText"]
                            MainLayout.levelText = MainLayout.TextFont.render(failText, True, MainLayout.TextColor)
                            return
                    
                    # Changes the image path but only if you have the required item
                    MainLayout.ChangeLevelImage(MainLayout.levelEvents["ChangeImageOnClick"]["NewImagePath"])

                    # Adds item if it has the key
                    if "AddItem" in MainLayout.levelEvents["ChangeImageOnClick"]:
                        Inventar.itemsDict[MainLayout.levelEvents["ChangeImageOnClick"]["AddItem"]["ItemName"]] = 1

                    # Disables the button if it has the key
                    if MainLayout.levelEvents["ChangeImageOnClick"]["disableAfterClick"]:
                        MainLayout.buttons[clickedButtonIndex].SetDisabled(True)
                        if clickedButtonIndex not in MainLayout.levelEvents["DisabledButtonIndexes"]:
                            MainLayout.levelEvents["DisabledButtonIndexes"].append(clickedButtonIndex)        

            ## LoadLevelOnClick
            if "LoadLevelOnClick" in MainLayout.levelEvents:
                for option in MainLayout.levelEvents["LoadLevelOnClick"]:
                    if option["buttonIndex"] == clickedButtonIndex:
                        MainLayout.TryLoadLevel(option["LevelName"])
