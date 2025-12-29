import turtle
from turtle import Turtle, Screen
# import colorgram
import random

leonardo = Turtle()
screen = Screen()
leonardo.shape("turtle")
leonardo.color("blue")

## Color Extraction from Image
# colors = colorgram.extract('Hirst.jpg', 15)
# colors_tuple = []
# for i in range(0, len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     rgb = (int(r), int(g), int(b))
#     colors_tuple.append(rgb)
# print(colors_tuple)

color_list = [(252, 250, 245), (253, 245, 250), (238, 252, 244), (237, 243, 251), (244, 229, 50), (202, 7, 33), (237, 228, 2), (193, 67, 24), (221, 151, 81), (36, 210, 91), (240, 41, 122), (35, 92, 177), (32, 31, 156), (205, 11, 5), (16, 18, 53)]
direction = [0, 90, 180, 270]
sides = 3

leonardo.pensize(1)
leonardo.speed('fastest')
turtle.colormode(255)

# Hirst
def hirst():
    x = 0
    leonardo.penup()
    leonardo.hideturtle()
    leonardo.setheading(220)
    leonardo.forward(300)
    leonardo.setheading(0)
    while x < 10:
        for i in range(0,  9):
            leonardo.dot(20, random.choice(color_list))
            leonardo.penup()
            leonardo.forward(50)
            leonardo.pendown()
            leonardo.dot(20, (random.choice(color_list)))
            leonardo.penup()
        x += 1
        for i in range(0, 1):
            leonardo.setheading(90)
            leonardo.forward(50)
            leonardo.setheading(180)
            leonardo.forward(450)
            leonardo.setheading(0)

hirst()

# Shape Draw
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        leonardo.forward(100)
        leonardo.right(angle)
#    leonardo.pencolor(random.choice(colors))

# for n_sides in range(3, 11):
#     draw_shape(n_sides)

# Random Walk
def random_walk():
    while True:
        random_direction = random.choice(direction)
        leonardo.forward(30)
        leonardo.setheading(random_direction)
        leonardo.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Spirograph Draw
def spiroraph():
    angle = 0
    while angle < 360:
        leonardo.circle(100)
        angle += 5
        leonardo.setheading(angle)
        leonardo.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen.exitonclick()

