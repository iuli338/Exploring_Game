from tkinter import BUTT
import pygame

class Button:

    # Static Members
    colorDict = {
        "Normal" : pygame.Color(90,90,90),  # Light Gray
        "Hover" : pygame.Color(168, 181, 224), # Pastel blue
        "Disabled" : pygame.Color(20,20,20) # Dark Gray
        }
    TextColor = pygame.Color(255,255,255)
    TextFont = None
    Padding = 5

    allButtons = []

    @staticmethod
    def Init():

        pygame.font.init()
        Button.TextFont = pygame.font.Font(None, 28)

    def __init__(self,position,text):
        # Initing the text
        self.text = text
        self.textSurface = Button.TextFont.render(text, True, Button.TextColor)
        # Initing the rect
        self.rect:pygame.Rect = self.textSurface.get_rect()
        # Calculating the padding
        self.rect.width = self.rect.width + Button.Padding * 2
        self.rect.height = self.rect.height + Button.Padding * 2
        # Initing the pisition
        self.rect.x = position[0]
        self.rect.y = position[1]
        # Initing the color
        self.color = Button.colorDict["Normal"]
        # Initing isDisabled to False
        self.isDisabled = False
        # Adding the instance to the static list
        Button.allButtons.append(self)

    @staticmethod
    def DrawAll(screen):
        for button in Button.allButtons:
            # Draw the rectangle
            pygame.draw.rect(screen, button.color, button.rect)
            # Draw the text surface
            screen.blit(button.textSurface, [button.rect.x+Button.Padding,button.rect.y+Button.Padding])

    @staticmethod
    def HandleMouseHower(mouseX,mouseY):
        for button in Button.allButtons:
            if button.isDisabled == False:
                if button.rect.collidepoint(mouseX,mouseY):
                    button.color = Button.colorDict["Hover"]
                    break
                else:
                    button.color = Button.colorDict["Normal"]

    def ChangeText(self,newText):
        # Changing the text
        self.text = newText
        self.text_surface = Button.TextFont.render(newText, True, Button.TextColor)
        # Updating the rect
        savedX, savedY = self.rect.topleft
        self.rect = self.text_surface.get_rect()
        self.rect.x = savedX
        self.rect.y = savedY

    def ChangePosition(self,newPos):
        self.rect.x = newPos[0]
        self.rect.y = newPos[1]

    def SetDisabled(self,state):
        self.isDisabled = state
        if state:
            self.color = Button.colorDict["Disabled"]
        else:
            self.color = Button.colorDict["Normal"]