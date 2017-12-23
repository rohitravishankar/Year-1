__author__ = 'Rohit Ravishankar'

"""
CSCI-603: Lab 1
Author: Rohit Ravishankar (rr9105@rit.edu)

This program prints my last name.
"""

import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def init():
    """
    Initialize for drawing.  (-300, -300) is in the lower left and
    (300, 300) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.title('LastName')

def drawR():
    """
    Draws the letter R.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (25,0), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(45)
    turtle.forward(math.sqrt(50))
    turtle.right(45)
    turtle.forward(15)
    turtle.right(45)
    turtle.forward(math.sqrt(50))
    turtle.right(45)
    turtle.forward(25)
    turtle.left(135)
    turtle.forward(36)
    turtle.penup()
    turtle.setheading(0)

def drawA():
    """
    Draws the letter A.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (12,22), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.left(60)
    turtle.forward(58)
    turtle.right(120)
    turtle.forward(58)
    turtle.penup()
    turtle.setheading(120)
    turtle.forward(25)
    turtle.left(60)
    turtle.pendown()
    turtle.forward(33)
    turtle.penup()
    turtle.setheading(0)

def drawV():
    """
    Draws the letter V.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (57,50), heading (east), up
    :return: None
    """
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    turtle.pendown()
    turtle.forward(58)
    turtle.left(120)
    turtle.forward(58)
    turtle.penup()
    turtle.setheading(0)

def drawI():
    """
    Draws the letter I.
    :pre: (relative) pos (0,0), heading (east), right
    :post: (relative) pos (0,50), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.forward(30)
    turtle.setheading(180)
    turtle.penup()
    turtle.forward(15)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.setheading(180)
    turtle.forward(30)
    turtle.penup()
    turtle.setheading(0)

def drawS():
    """
    Draws the letter S.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (25,50), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(math.sqrt(50))
    turtle.left(45)
    turtle.forward(15)
    turtle.left(45)
    turtle.forward(math.sqrt(50))
    turtle.left(45)
    turtle.forward(25)
    turtle.right(45)
    turtle.forward(math.sqrt(50))
    turtle.right(45)
    turtle.forward(15)
    turtle.right(45)
    turtle.forward(math.sqrt(50))
    turtle.right(45)
    turtle.forward(25)
    turtle.penup()
    turtle.setheading(0)

def drawH():
    """
    Draws the letter H.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (35,0), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.forward(50)
    turtle.penup()
    turtle.setheading(0)

def drawN():
    """
    Draws the letter N.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (40,50), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(70)
    turtle.left(135)
    turtle.forward(50)
    turtle.penup()
    turtle.setheading(0)

def drawK():
    """
    Draws the letter K.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (30,0), heading (east), up
    :return: None
    """
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(135)
    turtle.forward(35)
    turtle.left(180)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.setheading(0)

def main():
    init()
    turtle.penup()
    turtle.setposition(-275,0)
    drawR()
    turtle.setposition(-235,0)
    drawA()
    turtle.setposition(-185,0)
    drawV()
    turtle.setposition(-120,0)
    drawI()
    turtle.setposition(-75,0)
    drawS()
    turtle.setposition(-30,0)
    drawH()
    turtle.setposition(20,0)
    drawA()
    turtle.setposition(90,0)
    drawN()
    turtle.setposition(155,0)
    drawK()
    turtle.setposition(190,0)
    drawA()
    turtle.setposition(260,0)
    drawR()
    turtle.setposition(300,0)
    turtle.mainloop()

if __name__ == '__main__':
    main()

