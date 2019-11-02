import pygame
import sys
import numpy as np
from pygame import gfxdraw
from colorHandler import *

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

            if diX < 0: diX = diX + 2 * dyAbs

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

            if diY <= 0: diY = diY + 2 * dxAbs

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
    
        if dyAbs <= dxAbs: self.drawLineX(x1, y1, x2, y2, color)
        else: self.drawLineY(x1, y1, x2, y2, color)

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

    def drawTriangle(self, x1, y1, increment, color):
        self.drawLine(x1, y1 - increment, x1 + increment,  y1 + increment, color)
        self.drawLine(x1 - increment, y1 + increment, x1, y1 - increment, color)
        self.drawLine(x1 + increment, y1 + increment, x1 - increment, y1 + increment, color)

    def drawCurve(self, p0, p1, p2, p3, color):
        sX, sY = p0

        for t in np.arange(0,1,0.01):
            b0 = (1-t)**3
            b1 = 3 * t * (1-t)**2
            b2 = 3 * t**2 * (1-t)
            b3 = t**3

            eX = int((b0 * p0[0]) + (b1 * p1[0]) + (b2 * p2[0]) + (b3 * p3[0]))
            eY = int((b0 * p0[1]) + (b1 * p1[1]) + (b2 * p2[1]) + (b3 * p3[1]))
            self.drawLine(sX, sY, eX, eY, color)
            sX,sY = (eX, eY)

        self.drawLine(sX, sY, p3[0], p3[1], color)

    def floodFill(self, x, y, width, height, newColor):
        try:
            prevColor = self.screen.get_at((x,y))

            if prevColor == newColor: return
            stack = [(x,y)]
            scanUp = scanDown = False

            while stack:
                x, y = stack.pop()
                x1 = x

                while x1 >= 0 and self.screen.get_at((x1, y)) == prevColor: 
                    x1 = x1 - 1

                x1 = x1 + 1
                scanUp = scanDown = False

                while x1 < width and self.screen.get_at((x1, y)) == prevColor:
                    self.screen.set_at((x1, y), newColor)

                    if not scanUp and y > 0 and self.screen.get_at((x1, y-1)) == prevColor:
                        stack.append((x1, y-1))
                        scanUp = True

                    elif scanUp and y > 0 and self.screen.get_at((x1, y-1)) != prevColor:
                        scanUp = False

                    if not scanDown and y < height-1 and self.screen.get_at((x1, y+1)) == prevColor:
                        stack.append((x1, y+1))
                        scanDown = True

                    elif scanDown and y < height-1 and self.screen.get_at((x1, y+1)) != prevColor:
                        scanDown = False
                    
                    x1 = x1 + 1

        except IndexError:
            return