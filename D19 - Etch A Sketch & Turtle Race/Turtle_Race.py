from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
x_cord = -225
y_cord = -120

race_start = False
race_end = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which Turtle will win the race? Enter a color: ").lower()

# Turtle Creation
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(x=x_cord, y=y_cord)
    y_cord += 50

if user_bet:
    race_start = True

while race_start and not race_end:
    for turtle in turtles:
        turtles[turtle].forward(random.randint(0,10))
        if turtles[turtle].xcor() > 230:
            race_end = True
            winner = turtles[turtle].pencolor()
            if user_bet == winner:
                print(f"You won! The winner is {winner}!")
            else:
                print(f"You lost! The winner is {winner}!")

screen.exitonclick()
