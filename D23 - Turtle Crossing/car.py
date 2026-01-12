from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()

