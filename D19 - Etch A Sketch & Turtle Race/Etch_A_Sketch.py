from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

tim.pensize(2)
tim.speed("fastest")
screen.colormode(255)
color_list = [(252, 250, 245), (253, 245, 250), (238, 252, 244), (237, 243, 251), (244, 229, 50), (202, 7, 33), (237, 228, 2), (193, 67, 24), (221, 151, 81), (36, 210, 91), (240, 41, 122), (35, 92, 177), (32, 31, 156), (205, 11, 5), (16, 18, 53)]

def move_forward():
    """Moves the turtle forward."""
    tim.forward(10)

def move_up():
    """Faces the turtle north and moves forward."""
    tim.setheading(90)
    move_forward()

def move_right():
    """Faces the turtle east and moves forward."""
    tim.setheading(0)
    move_forward()

def move_down():
    """Faces the turtle south and moves forward."""
    tim.setheading(270)
    move_forward()

def move_left():
    """Faces the turtle west and moves forward."""
    tim.setheading(180)
    move_forward()

def rotate_left():
    """Rotates the turtle to the left"""
    rotation = 10
    tim.left(rotation)

def rotate_right():
    """Rotates the turtle to the right"""
    rotation = 10
    tim.right(rotation)

def clear():
    """Resets the turtle to home (0,0) and clears the screen."""
    tim.home()
    tim.clear()

def pen_color():
    """Randomly changes the color of the pen."""
    tim.color(random.choice(color_list))

screen.listen()

# Pen
screen.onkey(key="p", fun=pen_color)

# Movement
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=move_forward)

# Rotation
screen.onkey(key="e", fun=rotate_right)
screen.onkey(key="q", fun=rotate_left)

# Reset
screen.onkey(key="c", fun=clear)

screen.exitonclick()
