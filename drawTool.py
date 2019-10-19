import pygame
import sys
from pygame import gfxdraw

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((400, 400), 0, 32)
screen.fill(WHITE)

pygame.display.flip()

def drawLineX(x1, y1, x2, y2):
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

    screen.set_at((x,y), BLACK)

    while x < limit:
        x = x + 1

        if diX < 0: 
            diX = diX + 2 * dyAbs

        else:
            y = y + increment
            diX = diX + 2 * (dyAbs - dxAbs)
        
        screen.set_at((x,y), BLACK)

def drawLineY(x1, y1, x2, y2):
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

    screen.set_at((x,y), BLACK) 

    while y < limit:
        y = y + 1

        if diY <= 0:
            diY = diY + 2 * dxAbs

        else:
            x = x + increment
            diY = diY + 2 * (dxAbs - dyAbs)

        screen.set_at((x,y), BLACK) 
   
def drawLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dxAbs = abs(dx)
    dyAbs = abs(dy)
    diX = 2 * dyAbs - dxAbs
    diY = 2 * dxAbs - dyAbs
 
    if dyAbs <= dxAbs:
        drawLineX(x1, y1, x2, y2)

    else:
        drawLineY(x1, y1, x2, y2)

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
                drawLine(sX, sY, x, y)
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                line = False
                
        pygame.display.update()
