from drawTool import *

class DrawToolInteface:
    def __init__(self, width=800, height=800):
        self.drawTool = DrawTool(width, height)
        self.colorButton = []
        self.options = []
        self.actualColor = (0,0,0)
        self.actualDrawMode = 0
        self.prevDrawMode = 0
        self.filledImage = pygame.image.load('images/filled.jpg').convert()
        self.unfilledImage = pygame.image.load('images/unfilled.jpg')
        self.actualCurve = []
        self.initialP1 = (150, 300)
        self.initialP2 = (350, 300)

        # Create the colors
        left = 10
        for i in range(8):
            c = pygame.Rect(left, 10, 20, 20)
            self.colorButton.append((c, colors[i]))
            left += 30
            pygame.draw.rect(self.drawTool.screen, colors[i], c)

        left = 10
        for i in range(8, 16):
            c = pygame.Rect(left, 40, 20, 20)
            self.colorButton.append((c, colors[i]))
            left += 30
            pygame.draw.rect(self.drawTool.screen, colors[i], c)

        # Create the button of the actual color
        c = pygame.Rect(left+10, 20, 34, 34)
        self.colorButton.append((c, colors[i]))
        pygame.draw.rect(self.drawTool.screen, colors[0], c, 2)
        c = pygame.Rect(left+17, 28, 20, 20)
        self.colorButton.append((c, colors[i]))
        pygame.draw.rect(self.drawTool.screen, colors[0], c)
                
        left += 80
        # Create option that draws line
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        pygame.draw.rect(self.drawTool.screen, RED, c, 2)
        self.drawTool.drawLine(331, 12, 366, 47, RED)

        left += 50
        # Create option that draws circles
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        self.drawTool.drawCircle(399, 30, 10, BLACK)
        pygame.draw.rect(self.drawTool.screen, BLACK, c, 2)

        left += 50
        # Create option that draws rectangles
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        self.drawTool.drawRectangle(434, 20, 465, 38, BLACK)
        pygame.draw.rect(self.drawTool.screen, BLACK, c, 2)

        left += 50
        # Create option that draws squares
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        self.drawTool.drawSquare(487, 17, 25, BLACK)
        pygame.draw.rect(self.drawTool.screen, BLACK, c, 2)

        left += 50
        # Create optin that draws triangles
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        self.drawTool.drawTriangle(550, 30, 15, BLACK)
        pygame.draw.rect(self.drawTool.screen, BLACK, c, 2)

        left += 50
        # Create option that draws curves
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        self.drawTool.drawCurve((583, 42), (600, 12), (600, 12), (612, 42), BLACK)
        pygame.draw.rect(self.drawTool.screen, BLACK, c, 2)
        
        left += 50
        # Create option that draws polylines
        c = pygame.Rect(left, 10, 40, 40)
        self.options.append(c)
        self.drawTool.drawLine(632, 46, 640, 30, BLACK)
        self.drawTool.drawLine(640, 30, 652, 46, BLACK)
        self.drawTool.drawLine(652, 46, 661, 18, BLACK)
        pygame.draw.rect(self.drawTool.screen, BLACK, c, 2)

        left += 120
        # Create the button that executes floodFill function
        c = self.unfilledImage.get_rect()
        c.center = (left, 30)
        self.options.append((c, BLACK))
        self.drawTool.screen.blit(self.unfilledImage, c)

        # Create the limit line
        self.drawTool.drawLine(0, 65, 800, 65, BLACK)

    def redrawOption(self, option, color):
        if option != 7:
            pygame.draw.rect(self.drawTool.screen, color, self.options[option], 2)

            if option == 0: self.drawTool.drawLine(331, 12, 366, 47, color)
            elif option == 1: self.drawTool.drawCircle(399, 30, 10, color)
            elif option == 2: self.drawTool.drawRectangle(434, 20, 465, 38, color)
            elif option == 3: self.drawTool.drawSquare(487, 17, 25, color)
            elif option == 4: self.drawTool.drawTriangle(550, 30, 15, color)
            elif option == 5: self.drawTool.drawCurve((583, 42), (600, 12), (600, 12), (612, 42), color)  
            else: 
                self.drawTool.drawLine(632, 46, 640, 30, color)
                self.drawTool.drawLine(640, 30, 652, 46, color)
                self.drawTool.drawLine(652, 46, 661, 18, color)
        else:
            # Only works for option 7 (floodFill)
            if color == RED:
                c = self.filledImage.get_rect()
                c.center = (750, 30)
                self.options[7] = (c, RED)
                self.drawTool.screen.blit(self.filledImage, c)

            elif color == BLACK:
                c = self.unfilledImage.get_rect()
                c.center = (750, 30)
                self.options[7] = (c, BLACK)
                self.drawTool.screen.blit(self.unfilledImage, c)

    def main(self):
        draw = False
        polyline = False
        moveP1 = False
        moveP2 = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    break

                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    cX, cY = event.pos
                    
                    # Check if click is within the options pallete
                    if cY <= 65:
                        # Change the color of the actual color
                        for i in range(0, 16):
                            if self.colorButton[i][0].collidepoint(event.pos):
                                self.actualColor = self.colorButton[i][1]
                                pygame.draw.rect(self.drawTool.screen, self.colorButton[i][1], self.colorButton[16][0],2)
                                pygame.draw.rect(self.drawTool.screen, self.colorButton[i][1], self.colorButton[17][0])
                        
                        # Change the draw mode
                        if self.options[7][0].collidepoint(event.pos):
                            if self.options[7][1] == BLACK:
                                self.prevDrawMode = self.actualDrawMode
                                self.actualDrawMode = 7
                                self.redrawOption(self.prevDrawMode, BLACK)
                                c = self.filledImage.get_rect()
                                c.center = (750, 30)
                                self.options[7] = (c, RED)
                                self.drawTool.screen.blit(self.filledImage, c)

                            else:
                                self.prevDrawMode = self.actualDrawMode
                                self.actualDrawMode = 7
                                c = self.unfilledImage.get_rect()
                                c.center = (750, 30)
                                self.options[7] = (c, BLACK)
                                self.drawTool.screen.blit(self.unfilledImage, c)

                        for i in range(7):
                            if self.options[i].collidepoint(event.pos):
                                self.prevDrawMode = self.actualDrawMode
                                self.actualDrawMode = i
                                self.redrawOption(self.prevDrawMode, BLACK)
                                self.redrawOption(self.actualDrawMode, RED)

                    elif polyline:
                        sX, sY = eX, eY
                        self.drawTool.layer.blit(self.drawTool.screen, (0,0))

                    elif self.actualDrawMode == 7:
                        # Execute flood fill
                        cX, cY = event.pos
                        self.drawTool.floodFill(cX, cY, self.drawTool.screenSize[0], self.drawTool.screenSize[1], self.actualColor)

                    else:
                        sX, sY = event.pos
                        draw = True
                        self.drawTool.layer.blit(self.drawTool.screen, (0,0))

                        if len(self.actualCurve) > 0: self.actualCurve = []
                
                elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT and draw:
                    draw = False
                    polyline = False

                    if self.actualDrawMode == 5:
                        # In case of curve, save the actual curve
                        self.actualCurve = [(sX, sY), self.initialP1, self.initialP2, (eX, eY)] 
                
                elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT and not draw and not moveP1 and not moveP2:
                    # Enable moviment of P1 or P2
                    x,y = event.pos
                    
                    if len(self.actualCurve) > 0:
                        if x >= self.actualCurve[1][0] and x <= self.actualCurve[1][0] + 5 and y >= self.actualCurve[1][1] and y <= self.actualCurve[1][1] + 5:
                            moveP1 = True
                            moveP2 = False

                        elif x >= self.actualCurve[2][0] and x <= self.actualCurve[2][0] + 5 and y >= self.actualCurve[2][1] and y <= self.actualCurve[2][1] + 5:
                            moveP1 = False
                            moveP2 = True
                
                elif event.type == pygame.MOUSEMOTION and not draw:
                    # Move P1 or P2
                    if moveP1:
                        x,y = event.pos

                        if y <= 65: y = 65

                        self.actualCurve[1] = (x,y)
                        self.drawTool.screen.blit(self.drawTool.layer, (0,0))
                        self.drawTool.drawCurve(self.actualCurve[0], self.actualCurve[1], self.actualCurve[2], self.actualCurve[3], self.actualColor)
                        self.drawTool.drawSquare(self.actualCurve[1][0], self.actualCurve[1][1], 5, RED)
                        self.drawTool.drawSquare(self.actualCurve[2][0], self.actualCurve[2][1], 5, RED)

                    elif moveP2:
                        x,y = event.pos

                        if y <= 65: y = 65

                        self.actualCurve[2] = (x,y)
                        self.drawTool.screen.blit(self.drawTool.layer, (0,0))
                        self.drawTool.drawCurve(self.actualCurve[0], self.actualCurve[1], self.actualCurve[2], self.actualCurve[3], self.actualColor)
                        self.drawTool.drawSquare(self.actualCurve[1][0], self.actualCurve[1][1], 5, RED)
                        self.drawTool.drawSquare(self.actualCurve[2][0], self.actualCurve[2][1], 5, RED)

                elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
                    # Disable the moviment from P1 or P2
                    if moveP1: moveP1 = False
                    elif moveP2: moveP2 = False

                elif event.type == pygame.MOUSEMOTION and draw and not moveP1 and not moveP2:
                    eX, eY = event.pos

                    self.drawTool.screen.blit(self.drawTool.layer, (0,0))

                    if self.actualDrawMode == 0:
                        # Draw line
                        if eY <= 65: eY = 65
                        self.drawTool.drawLine(sX,sY, eX, eY, self.actualColor)

                    elif self.actualDrawMode == 1:
                        # Draw circle
                        r = int((((eX - sX)**2) + ((eY - sY)**2))**0.5)

                        if sY - r <= 65: r = sY - 66
                        self.drawTool.drawCircle(sX, sY, r, self.actualColor)

                    elif self.actualDrawMode == 2:
                        # Draw rectangle
                        if eY <= 65: eY = 67
                        self.drawTool.drawRectangle(sX, sY, eX, eY, self.actualColor)

                    elif self.actualDrawMode == 3:
                        # Draw square
                        increment = int((((eX - sX)**2) + ((eY - sY)**2))**0.5)
                        self.drawTool.drawSquare(sX, sY, increment, self.actualColor)

                    elif self.actualDrawMode == 4:
                        # Draw triangle
                        increment = int((((eX - sX)**2) + ((eY - sY)**2))**0.5)

                        if sY - increment <= 65: increment = sY - 66
                        self.drawTool.drawTriangle(sX, sY, increment, self.actualColor)

                    elif self.actualDrawMode == 5:
                        # Draw curve
                        if eY <= 65: eY = 65
                        self.initialP1 = (sX, sY)
                        self.initialP2 = (eX, eY)
                        self.drawTool.drawCurve((sX, sY), self.initialP1, self.initialP2, (eX, eY), self.actualColor)
                        self.drawTool.drawSquare(self.initialP1[0], self.initialP1[1], 5, RED)
                        self.drawTool.drawSquare(self.initialP2[0], self.initialP2[1], 5, RED)

                    elif self.actualDrawMode == 6:
                        # Draw polyline
                        polyline = True

                        if eY <= 65: eY = 65
                        self.drawTool.drawLine(sX,sY, eX, eY, self.actualColor)

                    else: continue

            pygame.display.flip()

if __name__ == '__main__':
    drawToolInteface = DrawToolInteface(800, 600)
    drawToolInteface.main()