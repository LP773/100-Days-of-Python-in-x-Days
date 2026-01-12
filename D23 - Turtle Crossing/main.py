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

difficulty = 10

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    car.load_car()
    car.move_cars()

    # Scoring/Finish Line Detection
    if player.ycor() > 280:
        player.reset_position()
        car.increase_speed()
        scoreboard.increase_score()

    # Detecting Collision
    for cars in car.all_cars:
        if cars.distance(player) < 25:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
