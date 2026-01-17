import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answers = []

answer_state = screen.textinput(title="Guess The State", prompt="Enter a State: ").title()
data = pandas.read_csv("50_states.csv")
answer_row = data[data["state"] == answer_state]

if answer_state == data["state"]:
    turtle.write(f"{answer_state}")
    x_cor = answer_row["x"].iloc[0]
    y_cor = answer_row["y"].iloc[0]
    turtle.goto(x_cor, y_cor)
