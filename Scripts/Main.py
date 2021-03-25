#   "\Для Ігри\Arcade\Main.py" Валік
import pygame

import Data

pygame.init()

mainWin = pygame.display.set_mode((1120, 630))
Data.addOptions()

# Player Options Cube
x = 50
y = 50
width = 30
height = 30
speed = 0.4
gravity = 0.2
jumpCount = 0
isJump = False

# Main Cicle
play = True
while play:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 1120 - width:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 630 - height:
        y += speed



    mainWin.fill((0, 0, 0))
    pygame.draw.rect(mainWin, (0, 0, 255), (x, y, width, height))
    pygame.display.update()
    pygame.time.delay(1)
    play = Data.closeProgram()

pygame.quit()
