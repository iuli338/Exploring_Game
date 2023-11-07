import pygame
import sys
from Button import Button
from MainLayout import MainLayout
from Level import Level

def DrawEverything(screen):
    MainLayout.Draw(screen)
    Button.DrawAll(screen)
    

def HandleOtherEvents(event):
    mouseX, mouseY = pygame.mouse.get_pos()
    Button.HandleMouseHower(mouseX,mouseY)
    MainLayout.HandleButtonsClick(event,mouseX,mouseY)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1024, 800

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exploring Game")

# Init Everything
Button.Init()
MainLayout.Init(screen)
Level.CreateLevels()
MainLayout.LoadLevel(Level.allLevels[0])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        HandleOtherEvents(event)

    # Fill the screen with a white background
    screen.fill((0,0,0))

    DrawEverything(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
