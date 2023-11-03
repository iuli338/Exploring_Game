import pygame
from Button import Button

class MainLayout:

    locationName = None
    locationImage = None
    locationText = None
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
        MainLayout.locationImage = pygame.Rect(imagePosition,imageSize)

        # Initing the locationName
        MainLayout.locationName = MainLayout.TextFont.render("Location name:", True, MainLayout.TextColor)
        MainLayout.locationText = MainLayout.TextFont.render("Text text text...", True, MainLayout.TextColor)

        # Initing the buttons
        firstButtonPos = [MainLayout.locationImage.x,MainLayout.locationImage.y+MainLayout.locationImage.height+42]
        MainLayout.buttons.append(Button(firstButtonPos,"Alegere 1"))
        firstButtonPos[1] += 40
        MainLayout.buttons.append(Button(firstButtonPos,"Alegere 2"))
        firstButtonPos[1] += 40
        MainLayout.buttons.append(Button(firstButtonPos,"Alegere 3"))

    def Draw(screen):
        # locationImage
        pygame.draw.rect(screen, MainLayout.TextColor, MainLayout.locationImage)
        # locationName
        locationNamePos = [MainLayout.locationImage.x,MainLayout.locationImage.y-28]
        screen.blit(MainLayout.locationName,locationNamePos)
        # locationText
        locationTextPos = [MainLayout.locationImage.x,MainLayout.locationImage.y+MainLayout.locationImage.height+10]
        screen.blit(MainLayout.locationText,locationTextPos)
        