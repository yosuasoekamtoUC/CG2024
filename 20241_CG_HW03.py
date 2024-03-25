import pygame
from pygame.locals import *
from sys import exit
import numpy as np

background_image_filename = 'image/curve_pattern.png'
sprite_image_filename = 'image/icon_speech.png'

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def drawPoint(pt, color, thick):
    pygame.draw.circle(screen, color, pt, thick)

def formula1(pt0, pt1, color, steps, thick):
    # 1. y = (y1 - y0) / (x1 - x0) * (Xi - x0) + y0
    x0, y0 = pt0[0], pt0[1]
    x1, y1 = pt1[0], pt1[1]
    if (x0 > x1):
        steps *= -1
    for Xi in np.arange(x0, x1, steps):
        Yi = (y1 - y0) / (x1 - x0) * (Xi - x0) + y0
        drawPoint(np.array([Xi, Yi]), color, thick)

def formula2(pt0, pt1, color, steps, thick):
    #2. coordinate free system = (a0 * p0) + (a1 * p1)
    x0, y0 = pt0[0], pt0[1]
    x1, y1 = pt1[0], pt1[1]
    for a in np.arange(0, 1, steps):
        new_point = (1 - a) * pt0 + a * pt1
        drawPoint(new_point, color, thick)

# HW2 implement drawLine with drawPoint
def drawLine(pt0, pt1, color, thick):
    pt0 = np.array(pt0, dtype = np.float32)
    pt1 = np.array(pt1, dtype = np.float32)

    drawPoint(pt0, color, thick)
    drawPoint(pt1, color, thick)
    steps = 0.01

    # 1. y = (y1 - y0) / (x1 - x0) * (Xi - x0) + y0
    # formula1(pt0, pt1, 'RED', steps, thick)

    # 2. coordinate free system = (a0 * p0) + (a1 * p1)
    formula2(pt0, pt1, color, steps, thick)

def drawPolylines(color, thick, clickCount):
    if clickCount < 2:
        return
    for i in range(clickCount - 1):
        drawLine(pts[i], pts[i + 1], color, thick)


if __name__ == '__main__':
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height), 0, 32)

    background = pygame.image.load(background_image_filename).convert()
    width, height = background.get_size()
    screen = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption("20235164-CompGraphHW03")
    screen.fill(WHITE)
    clock = pygame.time.Clock()

    loop = True
    press = False
    barycentric = False
    margin = 5

    pts = []
    clickCount = 0
    while loop:
        try:
            for event in pygame.event.get():
                press = False
                if event.type == pygame.QUIT:
                    loop = False

            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            pygame.draw.circle(screen, RED, pt, 0)

            # PRESS LEFT MOUSE - CREATE POINTS
            if event.type == pygame.MOUSEBUTTONDOWN and press == False and event.button == 1:
                press = True
                pts.append(pt)
                clickCount += 1

                if clickCount < 3:
                    pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    drawPolylines(GREEN, 1, clickCount)
                elif clickCount == 3:
                    pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    drawPolylines(GREEN, 1, clickCount)
                    drawLine(pts[0], pts[2], GREEN, 1)
                else:
                    pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)

            # RELEASE LEFT MOUSE
            if event.type == pygame.MOUSEBUTTONUP:
                press == False


            pygame.display.update()
            time_passed = clock.tick(1000)
        except Exception as e:
            print(e)
            pygame.quit()

    pygame.quit()