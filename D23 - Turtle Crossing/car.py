from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def load_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            random_y = random.randint(-250, 250)
            car.goto(x=290, y=random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
