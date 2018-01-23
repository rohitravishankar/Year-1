__author__ = 'Rohit Ravishankar'

import turtle

#Window size
WINDOW_WIDTH = 5000
WINDOW_HEIGHT = 5000

COLORS = [ 'brown', 'green', 'yellow', 'red', 'blue', 'orange', 'magenta', 'cyan', 'pink']

def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.setheading(90)
    turtle.tracer(0,0)
    turtle.title("Recursive Tree")


#Branch Angle
BRANCH_ANGLE = 45

def drawTree(segments, size):
    turtle.pensize(segments+1)
    turtle.pencolor(COLORS[segments])
    if segments < 1:
        return

    turtle.forward(size)
    turtle.left(BRANCH_ANGLE)
    drawTree(segments-1, size/2)
    turtle.right(BRANCH_ANGLE)

    turtle.right(BRANCH_ANGLE)
    drawTree(segments-1,size/2)
    turtle.left(BRANCH_ANGLE)
    turtle.penup()
    turtle.backward(size)
    turtle.pendown()


def main():
    init()
    drawTree(10,500)
    turtle.mainloop()

if __name__ == '__main__':
        main()