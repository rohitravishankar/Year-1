__author__ = 'Rohit Ravishankar'
__author__ = 'Parinitha Nagaraja'

"""
CSCI-603: Lab 1
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4872@rit.edu)

This program creates a forest scene
"""

import turtle
import math
import random

# global constants for window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
HOUSE = 'n'
TOTAL_WOOD_FROM_TREES = 0

def init():
    """
    Initialize for drawing.  (-300, -300) is in the lower left and
    (300, 300) is in the upper right.
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(180)
    turtle.forward(260)
    turtle.setheading(0)
    turtle.title('Forest')

def drawStar(tallestTreeHeight):
    """
    Draws a star in the night
    :param tallestTreeHeight: Height of the tallest tree
    :return: None
    :pre: (relative) pos (lastTreePosition,tallestTreeHeight+40), heading (north), backward
    :post: (relative) pos (lastTreePosition,tallestTreeHeight+40)
    """
    turtle.up()
    turtle.backward(tallestTreeHeight+40)
    turtle.down()
    for x in range(8):
        turtle.forward(10)
        turtle.backward(10)
        turtle.right(45)

def drawHouseHelper(lengthOfWall):
    """
    Helper function to draw the house
    :param lengthOftheWall: length of the wall
    :return:    None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(lengthOfWall)
    turtle.right(45)
    turtle.forward((lengthOfWall / 2) * math.sqrt(2))
    turtle.right(90)
    turtle.forward((lengthOfWall / 2) * math.sqrt(2))
    turtle.right(45)
    turtle.forward(lengthOfWall)
    turtle.right(90)
    turtle.forward(lengthOfWall)
    turtle.setheading(0)


def drawHouse(lengthOfWall, isDayOrNight):
    """
    Draws a house
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,100/lumberAvailable), heading (east), up
    :param lengthOfWall: Vertical length of the house
    :param isDayOrNight: To mark day or night
    :return: None
    """
    if isDayOrNight == "night":
        drawHouseHelper(100)
        turtle.forward(100)
    else:
        print('We will build a house with walls {0} tall'.format(lengthOfWall))
        turtle.up()
        turtle.goto(-160, 0)
        drawHouseHelper(lengthOfWall)
        turtle.up()
        turtle.forward(lengthOfWall)


def spacing():
    """
    Draws all objects with a space of 100
    :return: None
    """
    turtle.down()
    turtle.setheading(0)
    turtle.forward(100)
    turtle.up()

def treeTrunk(height):
    """
    Draws a tree trunk
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,Height), heading (north), up
    :param height: Height of the tree trunk
    :return: None
    """
    turtle.setheading(90)
    turtle.down()
    turtle.forward(height)
    turtle.up()

def pineTree(height):
    """
    Draws a triangle on the top of the trunk
    :param height: Height of the tree trunk
    :return: None
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (south), up
    """
    treeTrunk(height)
    turtle.down()
    turtle.right(90)
    turtle.forward((10*2)/math.sqrt(3))
    turtle.left(120)
    turtle.forward((20*2)/math.sqrt(3))
    turtle.left(120)
    turtle.forward((20*2)/math.sqrt(3))
    turtle.left(120)
    turtle.forward((10*2)/math.sqrt(3))
    turtle.right(90)
    turtle.forward(height)
    turtle.up()

def cedarTree(height):
    """
    Draws a square on top of the trunk
    :param height: Height of the tree trunk
    :return: None
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (south), up
    """
    treeTrunk(height)
    turtle.down()
    turtle.setheading(0)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(height)
    turtle.up()

def mapleTree(height):
    """
    Draws a circle on top of the tree trunk
    :param height: Height of the tree trunk
    :return: None
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (south), up
    """
    treeTrunk(height)
    turtle.down()
    turtle.setheading(0)
    turtle.circle(10)
    turtle.right(90)
    turtle.forward(height)
    turtle.up()


def drawTree(typeTree):
    """
    Draws a tree based on type
    :param typeTree: Height of the tree trunk
    :return height: Height of tree
    """
    if typeTree == 0 :
        height = random.randint(50,200)
        pineTree(height)
    elif typeTree == 1 :
        height = random.randint(50,150)
        mapleTree(height)
    else :
        height = random.randint(50, 100)
        cedarTree(height)
    return height

def tallestTree(height, maxHeight):
    """
    Returns the height of the which tree is more
    :param height: current tree height
    :param maxHeight: maximum height
    :return: maximum height
    """
    if height > maxHeight :
        maxHeight = height
    return maxHeight

def drawSun(heightOfWall):
    """
    Draws the sun during the day
    :param heightOfWall: To calculate the height of the sun
    :return: None
    :pre: (relative) pos (housePosition,heightOfSun), heading (north), backward
    :post: (relative) pos (housePosition,housePosition)
    """
    heightOfSun = heightOfWall + ((heightOfWall / 2) * math.sqrt(2)) + 20
    turtle.up()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(heightOfSun)
    turtle.down()
    turtle.circle(20)

def drawDay(totalWoodFromTrees, isHouseThere):
    """
    To draw the scene during the day
    :param totalWoodFromTrees: To calculate total wood from trees
    :param isHouseThere: Does a house need to be made
    :return: None
    """
    turtle.reset()
    turtle.showturtle()
    totalWood = 0
    lengthOfOneWall = 0
    global HOUSE
    if HOUSE == 'n':
        totalWood = TOTAL_WOOD_FROM_TREES
    elif HOUSE == 'y':
        totalWood = 200 + (50*math.sqrt(2)) + (50*math.sqrt(2)) + TOTAL_WOOD_FROM_TREES
    print('We have {0} units of lumber for building'.format(totalWood))
    lengthOfOneWall = totalWood/(2+math.sqrt(2))
    drawHouse(lengthOfOneWall,"day")
    drawSun(lengthOfOneWall)
    turtle.hideturtle()
    print('Day is done, house is built, click to quit')
    turtle.exitonclick()

def drawNight():
    """
    To draw the night scene
    :return: None
    """
    global TOTAL_WOOD_FROM_TREES
    TOTAL_WOOD_FROM_TREES = 0
    maxHeight = 0
    numberOfTrees = input("How many trees in your forest?")
    while int(numberOfTrees) < 2:
        numberOfTrees = input("How many trees in your forest?")
    global HOUSE
    HOUSE = input("Is there a house in the forest (y/n)?")
    for x in range(0,int(numberOfTrees)):
        height = drawTree(random.randint(0, 2))

        """There should be spacing between trees if it isn't the last tree"""
        if x != (int(numberOfTrees) - 1):
            spacing()
        if x == 0 and HOUSE == 'y':
            drawHouse(100,"night")
            spacing()
        TOTAL_WOOD_FROM_TREES += height
        maxHeight = tallestTree(height, maxHeight)
    drawStar(maxHeight)
    turtle.hideturtle()

def main():
    init()
    drawNight()
    print('Night is done, press enter for day')
    print('Click on screen to continue...')
    turtle.onscreenclick(drawDay)
    turtle.mainloop()


if __name__ == '__main__':
    main()
