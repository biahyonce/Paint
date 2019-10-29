import pygame
import sys
import numpy as np
from pygame import gfxdraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (210,210,210)
LEFT = 1
RIGHT = 3

colors = [
    (0,0,0),
    (255, 0, 0),
    (0, 255, 0),
    (255,255,0),
    (255, 0, 255),
    (0, 64, 255),
    (255, 128, 0),
    (153, 51, 102),
    (102,102,102),
    (0, 153,204),
    (153, 102, 0),
    (0,0,102),
    (0, 204, 255),
    (102, 0, 204),
    (255,255,204),
    (51, 153, 102)
]

class DrawTool:
    def __init__(self, width=800, height=800):
        pygame.init()

        self.screenSize= (width,height)
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.layer = pygame.surface.Surface((width,height))
        self.layer.blit(self.screen, (0,0))
        self.screen.fill(WHITE)
        self.layer.fill(WHITE)

        pygame.display.flip()
        
    def drawLineX(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        dxAbs = abs(dx)
        dyAbs = abs(dy)
        diX = 2 * dyAbs - dxAbs
        diY = 2 * dxAbs - dyAbs

        if dx >= 0: x,y,limit = x1, y1, x2   # Left -> Right
        else: x,y,limit = x2, y2, x1         # Right -> Left

        if (dx < 0 and dy < 0) or (dx > 0 and dy > 0): increment = 1
        else: increment = -1

        self.screen.set_at((x,y), color)

        while x < limit:
            x = x + 1

            if diX < 0: 
                diX = diX + 2 * dyAbs

            else:
                y = y + increment
                diX = diX + 2 * (dyAbs - dxAbs)
            
            self.screen.set_at((x,y), color)

    def drawLineY(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        dxAbs = abs(dx)
        dyAbs = abs(dy)
        diX = 2 * dyAbs - dxAbs
        diY = 2 * dxAbs - dyAbs

        if dy >= 0: x, y, limit = x1, y1, y2   # Down -> Top
        else: x, y, limit = x2, y2, y1         # Top -> Down

        if (dx < 0 and dy < 0) or (dx > 0 and dy > 0): increment = 1
        else: increment = -1

        self.screen.set_at((x,y), color) 

        while y < limit:
            y = y + 1

            if diY <= 0:
                diY = diY + 2 * dxAbs

            else:
                x = x + increment
                diY = diY + 2 * (dxAbs - dyAbs)

            self.screen.set_at((x,y), color) 
    
    def drawLine(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        dxAbs = abs(dx)
        dyAbs = abs(dy)
        diX = 2 * dyAbs - dxAbs
        diY = 2 * dxAbs - dyAbs
    
        if dyAbs <= dxAbs:
            self.drawLineX(x1, y1, x2, y2, color)

        else:
            self.drawLineY(x1, y1, x2, y2, color)

    def drawSquare(self, x1, y1, increment, color):
        self.drawLine(x1, y1, x1, y1 + increment, color)
        self.drawLine(x1, y1, x1 + increment, y1, color)
        self.drawLine(x1, y1 + increment, x1 + increment, y1 + increment, color)
        self.drawLine(x1 + increment, y1 + increment, x1 + increment, y1, color)

    def drawRectangle(self, x1, y1, x2, y2, color):
        self.drawLine(x1, y1, x2, y1, color)
        self.drawLine(x2, y1, x2, y2, color)
        self.drawLine(x2, y2, x1, y2, color)
        self.drawLine(x1, y2, x1, y1, color)

    def drawCircle(self, x2, y2, r, color):
        x1 = 0
        y1 = r
        d = 1 - r

        self.plotCircleOctect(x1,y1, x2, y2, color)

        while y1 > x1:
            if d < 0: d += (2*x1) + 3
            else:
                d += 2 * (x1 - y1) + 5
                y1 = y1 - 1

            x1 = x1 + 1
            self.plotCircleOctect(x1, y1, x2, y2, color)

    def plotCircleOctect(self, x1, y1, x2, y2, color):
        self.screen.set_at((x1 + x2, y1 + y2), color)
        self.screen.set_at((x2 - y1, x1 + y2), color)
        self.screen.set_at((x2 - y1, y2 - x1), color)
        self.screen.set_at((x2 - x1, y2 - y1), color)
        self.screen.set_at((x2 - x1, y1 + y2), color)
        self.screen.set_at((x1 + x2, y2 - y1), color)
        self.screen.set_at((y1 + x2, y2 - x1), color)
        self.screen.set_at((y1 + x2, x1 + y2), color)

    def drawTriangle(self, x, y, increment, color):
        self.drawLine(x, y - increment, x + increment,  y + increment, color)
        self.drawLine(x - increment, y + increment, x, y - increment, color)
        self.drawLine(x + increment, y + increment, x - increment, y + increment, color)

    def drawCurve(self, p1, p2, p3, color):
        for t in np.arange(0, 1, 0.001):
            bx = int(p1[0] + (((1 - t) ** 2)*(p1[0] - p2[0])) + ((t**2) * (p3[0] - p1[0])))
            by = int(p1[1] + (((1 - t) ** 2)*(p1[1] - p2[1])) + ((t**2) * (p3[1] - p1[1])))
            self.screen.set_at((bx, by), color)


    def floodFillRecursive(self, x, y, prevColor, newColor):
        try:
            if x < 0 or x > 400 or y < 0 or y > 400: return
            if self.screen.get_at((x,y)) != prevColor: return

            self.screen.set_at((x,y), newColor)

            self.floodFill(x+1,y, newColor)
            self.floodFill(x,y+1, newColor)
            self.floodFill(x-1,y, newColor)
            self.floodFill(x,y-1, newColor)

        except IndexError:
            return

    def floodFill(self, x,y, newColor):
        try:
            prevColor = self.screen.get_at((x,y))

            if prevColor == newColor: return

            stack = [(x,y)]

            while stack:
                x,y = stack.pop()
                self.screen.set_at((x,y), newColor)

                if y - 1 > 0 and self.screen.get_at((x, y-1)) == prevColor: stack.append((x, y-1))
                if y + 1 < self.screenSize[1] and self.screen.get_at((x, y+1)) == prevColor: stack.append((x, y+1))
                if x - 1 > 0 and self.screen.get_at((x-1, y)) == prevColor: stack.append((x-1, y))
                if x + 1 < self.screenSize[0] and self.screen.get_at((x+1, y)) == prevColor: stack.append((x+1, y))

        except IndexError:
            return 
