import turtle
import math
import sys

# global array declaration for colors
COLORS = ['blue', 'red']

# Pen size
PEN_SIZE = 2

def drawSquareRed0(length):
    """
    Draw a red square of side length
    :param length: Side of the square
    :return: None
    """
    turtle.fillcolor('red')
    turtle.color('red')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()

def drawSquareBlue(L):
    """
    Draw a blue square with a red square on inside it
    :param L: Length of the side of the blue square
    :return: None
    """
    turtle.fillcolor('blue')
    turtle.color('blue')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(L)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.forward(L/2)
    turtle.left(45)
    turtle.down()
    alpha = math.sqrt( 2 * (L/2)**2 )
    drawSquareRed0(alpha)

def drawNestedSquares(length, depth):
    if depth < 1 :
        return 0
    else:
        sum = length * length
        color = COLORS[depth % 2 == 0]
        turtle.pensize(PEN_SIZE)
        turtle.fillcolor(color)
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(length)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(length/2)
        turtle.left(45)
        alpha = math.sqrt( 2 * (length/2)**2 )
        sum += drawNestedSquares(alpha,depth - 1)
    return sum

def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 squares.py depth length")
        exit(2)
    print(drawNestedSquares(int(sys.argv[2]), float(sys.argv[1])))
    turtle.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    main()
