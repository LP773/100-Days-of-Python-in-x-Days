import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_turtle = Turtle()
answer_turtle.hideturtle()
answer_turtle.penup()

# Game Tracking
answers = []
correct_guesses = 0

answer = screen.textinput(title="Guess The State", prompt="Enter a State: ").title()
data = pandas.read_csv("50_states.csv")
game_on = True

while game_on:
    row = data[data["state"] == answer]
    state = row.state.iloc[0]

    if answer == state:
        answers.append(row)
        x_cor = row.x.iloc[0]
        y_cor = row.y.iloc[0]
        answer_turtle.goto(x_cor, y_cor)
        answer_turtle.write(f"{answer}", True, align="center")
        answers.append(answer)
        correct_guesses += 1
        screen.update()
screen.exitonclick()
