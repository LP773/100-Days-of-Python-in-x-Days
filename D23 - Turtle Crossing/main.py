from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car import Car

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = Car()

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
