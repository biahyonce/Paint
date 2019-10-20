import pygame
import sys
from pygame import gfxdraw

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode((400, 400), 0, 32)
screen.fill(WHITE)

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

def drawCircle(x2, y2, r, color):
    x = 0
    y = r
    d = 1 - r

    plotCircleOctect(x,y, x2, y2, color)

    while y > x:
        if d < 0: d += (2*x) + 3
        else:
            d += 2 * (x - y) + 5
            y = y - 1

        x = x + 1
        plotCircleOctect(x,y, x2, y2, color)

def plotCircleOctect(x1, y1, x2, y2, color):
	screen.set_at((x1 + x2, y1 + y2), color)
	screen.set_at((x2 - y1, x1 + y2), color)
	screen.set_at((x2 - y1, y2 - x1), color)
	screen.set_at((x2 - x1, y2 - y1), color)
	screen.set_at((x2 - x1, y1 + y2), color)
	screen.set_at((x1 + x2, y2 - y1), color)
	screen.set_at((y1 + x2, y2 - x1), color)
	screen.set_at((y1 + x2, x1 + y2), color)

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

            if event.type == pygame.MOUSEMOTION and line:
                screen.fill(WHITE)
                x, y = event.pos

                # Calcula a distância entre pontos (define o raio)
                r = int((((x - sX)**2) + ((y - sY)**2))**0.5)
                drawCircle(sX, sY, r, BLACK)
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                line = False
        
        pygame.display.update()
