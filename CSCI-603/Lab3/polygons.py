__author__ = 'Rohit Ravishankar'
__author__ = 'Parinitha Nagaraja'

"""
CSCI-603: Lab 3
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4872@rit.edu)

This program draws recursive polygons
"""

import turtle
import sys
import random

#pen size to use for polygon
FILL_PEN_WIDTH = 1.5
UNFILL_PEN_WIDTH = 3

#"constants" used for color used at each depth
COLORS = 'red', 'orange', 'yellow', 'green', 'blue', 'blueviolet', 'Sea Green', 'Saddle Brown' ,'violet', 'turquoise', 'cyan','magenta','brown','peru','black'

# global constants for window dimensions
WINDOW_WIDTH = 10000
WINDOW_HEIGHT = 10000

#Length of the side
SIDE_LENGTH = 2000

def randomColorPicker():
    """
    Picks a random number between 0 and length of color array - 2
    :return: random number between 0 and 7
    """
    return random.randint(0,len(COLORS)-2)

def init():
    """
    Initialize for drawing.  (-5000, -5000) is in the lower left and
    (5000, 5000) is in the upper right.
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.tracer(0,0)
    turtle.setheading(0)
    turtle.title('Polygons')

    #Setting the position to write team member names
    turtle.goto(2250,4000)
    turtle.write("Rohit Ravishankar", True, align="left",font=("Arial", 16, "normal"))
    turtle.goto(2250,3750)
    turtle.write("Parinitha Nagaraja", True, align="left",font=("Arial", 16, "normal"))

def drawPolygonFill(numberOfSides, sideLength, angle):
    """
    Helper function to fill a polygon
    :param numberOfSides: Number of sides of a polygon
    :param sideLength: Length of the side of the polygon
    :param angle: Internal angle of the polygon
    :return: None
    """
    turtle.begin_fill()
    for _ in range(numberOfSides):
        turtle.pen(pencolor=COLORS[-1], pensize=FILL_PEN_WIDTH)
        turtle.left(angle)
        turtle.forward(sideLength)
    turtle.end_fill()

def drawPolygon(numberOfSides, sideLength, fillValue):
    """
    Draws filled and unfilled polygons recursively based on fillValue
    :param numberOfSides: Number of sides of the initial/largest polygon
    :param sideLength: Length of the side of the largest polygon
    :param fillValue: Should the polygon be filled or not

    :pre: (relative) pos (0,0), heading (east)
    :post: (relative) pos (0,0), heading (east)
    :return:
    """
    if numberOfSides < 3:
        return 0
    sum = numberOfSides * sideLength
    angle = 360 / numberOfSides
    if fillValue == "fill":
        turtle.fillcolor(COLORS[randomColorPicker()])
        drawPolygonFill(numberOfSides,sideLength,angle)
        for _ in range(numberOfSides):
            turtle.pen(pensize = FILL_PEN_WIDTH)
            turtle.left(angle)
            turtle.forward(sideLength)
            sum += drawPolygon(numberOfSides-1, sideLength/2, "fill")
    else:
        for _ in range(numberOfSides):
            turtle.pen(pencolor = COLORS[randomColorPicker()], pensize = UNFILL_PEN_WIDTH)
            turtle.left(angle)
            turtle.forward(sideLength)
            sum += drawPolygon(numberOfSides - 1, sideLength / 2, "unfill")
    return sum


def main():
    """
    Main calling function
    :return: None
    """
    init()

    #setting position to 0,0 after writing team member names for turtle to draw figure
    turtle.setposition(0,0);
    turtle.down()
    if len(sys.argv) < 3:
        print("\nMissing arguments")
        exit(22)
    print('Sum: ',drawPolygon(int(sys.argv[1]), SIDE_LENGTH,sys.argv[2]))
    turtle.up()
    turtle.mainloop()


if __name__ == '__main__':
    main()