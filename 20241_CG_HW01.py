import pygame
from pygame.locals import *
from sys import exit
import numpy as np

background_image_filename = 'image/curve_pattern.png'
sprite_image_filename = 'image/icon_speech.png'

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("20235164-CompGraphHW01")
    clock = pygame.time.Clock()

    loop = True
    press = False

    x1,y1, x2, y2 = 0, 0, 0, 0
    clickCount = 0
    while loop:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            px, py = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, (0, 0, 255), (px-5, py-5, 10, 10))
                if clickCount < 1:
                    x1 = px
                    y1 = py
                elif clickCount > 1:
                    x2 = px
                    y2 = py
                    pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2))
                    x1 = px
                    y1 = py
                clickCount += 1

            if event.type == pygame.MOUSEBUTTONUP:
                press == False
            pygame.display.update()
            clock.tick(1000)
        except Exception as e:
            print(e)
            pygame.quit()

    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
