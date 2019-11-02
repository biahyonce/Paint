## `Paint`

### `Installation`
```
pip3 install -r requirements.txt
git clone https://github.com/BiancaCristina/Paint.git
```

### `Basic Usage`
To open the Paint window, execute:
```
python3 src/drawToolInterface
```

There are six types of primitives for drawing: line, circle, rectangle, square, triangle, curve and polyline. Furthermore, it's possible to change colors and to fill drawings. Here are some tips about the tool:

#### `Line, Circle, Rectangle, Square and Triangle`
```
Click anywhere on the screen using the left button to define the start point of the primitive. 
Then, move the cursor around to choose the size of the primitive. 
After that, click anywhere on the screen using the right button to define the end point of the primitive. 
```

#### `Curve`
```
Click anywhere on the screen using the left button to define the start point of the curve, at the 
beginning a curve with curvature equal to 0 (segment) will be drawn. Then, move the cursor around
to choose the size of the curve. After that, click anywhere on the screen using the right button 
to define the end point of the curve. Next, when the curve with curvature equal to 0 is drawn, 
two red squares will be shown indicating the control points of the curve. To change the position 
of the control points and therefore the shape of the curve, just click on any of the squares 
using the right button and then drag the mouse around to change the position of the control point. 
After that, click anywhere on the screen using the right button to determine the control point 
location. Once a new curve begin to be drawn, it won't be possible to change the shape
of the previous curve. 
```

#### `Polyline`
```
Click anywhere on the screen using the left button to define the start point of the polyline. Then, drag 
the mouse around to determine the size of the first line drawn. To keep drawing lines, just click on the 
screen using the left button to begin a new line. When the polyline is done, click on the screen using 
the right button to define the end point of the polyline. 
```

#### `Color`
```
To change the color, just click on any of the colorful rectangles and the new color 
corresponding will be picked.
```

#### `Fill`
```
To fill some part of the screen, just click on the paint bucket and then select the area 
that will be filled. 
```

### `Usage as Library`
To incorporate the methods used in drawToolInterface to another project, just:
```python
from drawTool import *
```
For more information, read the complete [documentation](https://github.com/BiancaCristina/Paint/tree/master/docs).

