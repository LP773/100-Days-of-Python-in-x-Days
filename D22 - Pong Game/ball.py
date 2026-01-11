from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .8

    def reset(self, winner):
        if winner == True:
            rng = random.randint(0, 1)
            self.x_move = -10
            self.y_move = 10
            if rng == 0:
                self.y_move *= -1
            elif rng == 1:
                self.y_move *= 1

        elif winner == False:
            rng = random.randint(0, 1)
            self.x_move = 10
            self.y_move = 10
            if rng == 0:
                self.y_move *= -1
            elif rng == 1:
                self.y_move *= 1
        self.move_speed = 0.07
        self.goto(self.x_move, self.y_move)
