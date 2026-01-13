from os import write
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
HIGHSCORE_FILE = open("highscore.txt", mode="r")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(HIGHSCORE_FILE.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()
