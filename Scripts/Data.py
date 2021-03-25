import pygame
import os

# Знаходить шлях ігри в основну папку
gamePath = os.path.dirname(os.path.abspath(__file__)).replace("\Scripts", "")


def addOptions():
    programIcon = pygame.image.load(gamePath + '/icon.ico')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Arcade")


def closeProgram():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
