__author__ = 'sps'

"""
CSCI-603: Intro Lecture (week 1)
Author: Sean Strout (sps@cs.rit.edu)

This is a demo program that draws several Python heads.  It demonstrates
the importance of using a hierarchy of functions that can be re-used.
"""

import turtle

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init():
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.hideturtle()
    turtle.title('Snakes')
    turtle.speed(0)

def drawHead():
    """
    Draw the head outline.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    turtle.color('green')
    turtle.begin_fill()
    turtle.down()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(25)
    turtle.left(90)
    turtle.up()
    turtle.end_fill()

def drawTongue():
    """
    Draw the tongue.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    turtle.color('red')
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(60)
    turtle.down()
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(10)
    turtle.back(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.back(10)
    turtle.left(45)
    turtle.up()
    turtle.back(85)
    turtle.right(90)
    turtle.back(25)
    turtle.color('black')

def drawEyes():
    """
    Draw the pair of eyes.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    # left eye
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()

    # right eye
    turtle.forward(30)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()

    # return back
    turtle.back(30)
    turtle.left(90)
    turtle.back(10)
    turtle.right(90)
    turtle.back(10)

def drawNose():
    """
    Draw the nostrils.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(5)
    turtle.down()
    turtle.forward(1)
    turtle.back(1)
    turtle.up()
    turtle.back(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.down()
    turtle.forward(1)
    turtle.back(1)
    turtle.up()
    turtle.back(5)
    turtle.left(45)
    turtle.up()
    turtle.back(30)
    turtle.right(90)
    turtle.back(25)

def drawSnake():
    """
    Draw a single snake.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    drawHead()
    drawTongue()
    drawEyes()
    drawNose()

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    init()
    drawSnake()
    turtle.left(180)
    drawSnake()
    turtle.right(180)

    turtle.mainloop()

if __name__ == '__main__':
    main()