from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1 = 0
        self.p2 = 0
        self.goto(0,250)
        self.write(f"{self.p1} {self.p2}", align="center", font=("Courier", 50, "normal"))

    def increase_p1_score(self):
        self.p1 += 1
        self.clear()
        self.write(f"{self.p1} {self.p2}", align="center", font=("Courier", 50, "normal"))

    def increase_p2_score(self):
        self.p2 += 1
        self.clear()
        self.write(f"{self.p1} {self.p2}", align="center", font=("Courier", 50, "normal"))

    # def increase_score(self, winner):
    #     if winner == True:
    #         self.p1 += 1
    #         self.clear()
    #         self.write(f"{self.p1} {self.p2}", align="center", font=("Courier", 50, "normal"))
    #     else:
    #         self.p2 += 1
    #         self.clear()
    #         self.write(f"{self.p1} {self.p2}", align="center", font=("Courier", 50, "normal"))
