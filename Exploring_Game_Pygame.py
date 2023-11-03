import pygame
import sys
from Button import Button

def DrawEverything(screen):
    Button.DrawAll(screen)

def HandleOtherEvents(event):
    mouseX, mouseY = pygame.mouse.get_pos()
    Button.HandleMouseHower(mouseX,mouseY)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1024, 800

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exploring Game")

# Init Everything
Button.Init()

# Experimenting
but1 = Button((50,50),"Alegere 1")
but1.ChangePosition((200,200))

but2 = Button((300,300),"Dezactivat")
but2.SetDisabled(True)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    HandleOtherEvents(event)

    # Fill the screen with a white background
    screen.fill((40,40,40))

    DrawEverything(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
