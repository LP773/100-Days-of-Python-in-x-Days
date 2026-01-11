from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x_cor,y_cor)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def move_w(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_s(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
