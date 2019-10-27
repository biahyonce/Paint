import pygame
import sys
import numpy as np
from pygame import gfxdraw

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((400, 400), 0, 32)
layer = pygame.surface.Surface((400,400))
layer.blit(screen, (0,0))
screen.fill(WHITE)
layer.fill(WHITE)

pygame.display.flip()

def drawLineX(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    dxAbs = abs(dx)
    dyAbs = abs(dy)
    diX = 2 * dyAbs - dxAbs
    diY = 2 * dxAbs - dyAbs

    if dx >= 0: x,y,limit = x1, y1, x2   # Esq -> Dir
    else: x,y,limit = x2, y2, x1         # Dir -> Esq

    if (dx < 0 and dy < 0) or (dx > 0 and dy > 0): increment = 1
    else: increment = -1

    screen.set_at((x,y), color)

    while x < limit:
        x = x + 1

        if diX < 0: 
            diX = diX + 2 * dyAbs

        else:
            y = y + increment
            diX = diX + 2 * (dyAbs - dxAbs)
        
        screen.set_at((x,y), color)

def drawLineY(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    dxAbs = abs(dx)
    dyAbs = abs(dy)
    diX = 2 * dyAbs - dxAbs
    diY = 2 * dxAbs - dyAbs

    if dy >= 0: x, y, limit = x1, y1, y2   # Baixo -> Cima
    else: x, y, limit = x2, y2, y1         # Cima -> Baixo

    if (dx < 0 and dy < 0) or (dx > 0 and dy > 0): increment = 1
    else: increment = -1

    screen.set_at((x,y), color) 

    while y < limit:
        y = y + 1

        if diY <= 0:
            diY = diY + 2 * dxAbs

        else:
            x = x + increment
            diY = diY + 2 * (dxAbs - dyAbs)

        screen.set_at((x,y), color) 
   
def drawLine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    dxAbs = abs(dx)
    dyAbs = abs(dy)
    diX = 2 * dyAbs - dxAbs
    diY = 2 * dxAbs - dyAbs
 
    if dyAbs <= dxAbs:
        drawLineX(x1, y1, x2, y2, color)

    else:
        drawLineY(x1, y1, x2, y2, color)

def drawSquare(x1, y1, increment, color):
    drawLine(x1, y1, x1, y1 + increment, color)
    drawLine(x1, y1, x1 + increment, y1, color)
    drawLine(x1, y1 + increment, x1 + increment, y1 + increment, color)
    drawLine(x1 + increment, y1 + increment, x1 + increment, y1, color)

def drawRectangle(x1, y1, x2, y2, color):
    drawLine(x1, y1, x2, y1, color)
    drawLine(x2, y1, x2, y2, color)
    drawLine(x2, y2, x1, y2, color)
    drawLine(x1, y2, x1, y1, color)

def drawCircle(x2, y2, r, color):
    x1 = 0
    y1 = r
    d = 1 - r

    plotCircleOctect(x1,y1, x2, y2, color)

    while y1 > x1:
        if d < 0: d += (2*x1) + 3
        else:
            d += 2 * (x1 - y1) + 5
            y1 = y1 - 1

        x1 = x1 + 1
        plotCircleOctect(x1, y1, x2, y2, color)

def plotCircleOctect(x1, y1, x2, y2, color):
	screen.set_at((x1 + x2, y1 + y2), color)
	screen.set_at((x2 - y1, x1 + y2), color)
	screen.set_at((x2 - y1, y2 - x1), color)
	screen.set_at((x2 - x1, y2 - y1), color)
	screen.set_at((x2 - x1, y1 + y2), color)
	screen.set_at((x1 + x2, y2 - y1), color)
	screen.set_at((y1 + x2, y2 - x1), color)
	screen.set_at((y1 + x2, x1 + y2), color)

def drawTriangle(x, y, increment, color):
    drawLine(x, y - increment, x + increment,  y + increment, color)
    drawLine(x - increment, y + increment, x, y - increment, color)
    drawLine(x + increment, y + increment, x - increment, y + increment, color)

def drawCurve(p1, p2, p3, color):
    for t in np.arange(0, 1, 0.001):
        bx = int(p1[0] + (((1 - t) ** 2)*(p1[0] - p2[0])) + ((t**2) * (p3[0] - p1[0])))
        by = int(p1[1] + (((1 - t) ** 2)*(p1[1] - p2[1])) + ((t**2) * (p3[1] - p1[1])))
        screen.set_at((bx, by), color)

if __name__ == '__main__':
    sX = 0
    sY = 0
    line = False
    LEFT = 1
    RIGHT = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                sX, sY = event.pos
                line = True
                layer.blit(screen, (0,0))

            if event.type == pygame.MOUSEMOTION and line:
                x, y = event.pos
                screen.blit(layer, (0,0))
                drawLine(sX, sY, x, y, RED)

            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                line = False
        
        pygame.display.flip()
