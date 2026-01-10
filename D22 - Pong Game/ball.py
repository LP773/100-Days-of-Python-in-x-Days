from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x,new_y)
