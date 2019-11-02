## `DrawTool` module

### `DrawTool`
```
screenSize: tuple
screen: pygame.Surface
layer: pygame.Surface
```

#### `__init__`
Initialize the draw tool.

Params:
```
width: int (optional)
height: int (optional)
```

#### ` drawLineX`
Internal function that draws lines on x-axis (left to right or right to left) using Bresenham Algorithm. 

Params:
```
x1: int 
y1: int 
x2: int
y2: int
color: tuple
```

#### ` drawLineY`
Internal function that draws lines on y-axis (bottom up or top down) using Bresenham Algorithm. 

Params:
```
x1: int 
y1: int 
x2: int
y2: int
color: tuple
```

#### `drawLine `
Function that decides whether the line should be drawn on x-axis or y-axis using Bresenham Algorithm and call the corresponding function. 

Params:
```
x1: int 
y1: int 
x2: int
y2: int
color: tuple
```

#### ` drawSquare`
Function that draw square using the function "drawLine". 

Params:
```
x1: int
y1: int
increment: int
color: tuple
```

#### ` drawRectangle`
Function that draw rectangle using the function "drawLine".

Params:
```
x1: int
y1: int
increment: int
color: tuple
```

#### `drawCircle `
Function that draw circle using the Midpoint Circle Algorithm. 

Params:
```
x2: int
y2: int
r: int
color: tuple
```

#### ` plotCircleOctect`
Internal function that plot the octects of the circle using the Midpoint Circle Algorithm. 

Params:
```
x1: int
y1: int
x2: int
y2: int
color: tuple
```

#### ` drawTriangle`
Function that draw triangles using the function "drawLine". 

Params:
```
x1: int
y1: int
increment: int
```

#### ` drawCurve`
Function that draws curves using the Cubic Bezier. 

Params:
```
p0: tuple
p1: tuple
p2: tuple
p3: tuple
color: tuple
```

#### ` floodFill`
Function that fill using the Scanline Flood Fill Algorithm.

Params:
```
x: int
y: int
width: int
height: int
newColor: tuple
```
