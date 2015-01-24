# The functions required to draw the game board and indicate where
# the characters are on the board will be defined here.

import turtle

def draw_board():

    # Set up and outline of board

    board = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-110, -110, 110, 110)
    board.up()
    board.goto(-100, -100)
    board.down()

    for sides in range(4):
        board.forward(200)
        board.left(90)

    # Draw indivual rooms

    # Conservatory
    board.forward(55)
    board.left(90)
    board.forward(40)
    board.left(90)
    board.forward(55)

    # Billiard Room
    board.right(90)
    board.forward(20)
    board.right(90)
    board.forward(55)
    board.left(90)
    board.forward(30)
    board.left(90)
    board.forward(55)

    # Library Room
    board.right(90)
    board.forward(20)
    board.right(90)
    board.forward(55)
    board.left(90)
    board.forward(30)
    board.left(90)
    board.forward(55)

    # Study

    board.right(90)
    board.forward(20)
    board.right(90)
    board.forward(55)
    board.left

    wn.exitonclick()

draw_board()
