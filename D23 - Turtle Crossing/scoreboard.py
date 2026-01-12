from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-235,270)
        self.write(f"Level: {self.score}", align="center", font=FONT)
