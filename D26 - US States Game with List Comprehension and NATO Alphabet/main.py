import turtle
from turtle import Turtle, Screen
import pandas

# Screen and Turtle Setup
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)

answer_turtle = Turtle()
answer_turtle.hideturtle()
answer_turtle.penup()

answers = []

answer = screen.textinput(title="Guess The State", prompt="Enter a State: ").title()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

#game_on = True

# While this is my solution originally, it made more sense to track answers being less than 50.
# Lines 30-40 would not work if there was a typo (misspelled state)

#while game_on:
while len(answers) < 50:
    # row = data[data["state"] == answer]
    # state = row.state.iloc[0]

    # if answer == state:
    #     x_cor = row.x.iloc[0]
    #     y_cor = row.y.iloc[0]
    #     answer_turtle.goto(x_cor, y_cor)
    #     answer_turtle.write(f"{answer}", True, align="center")
    #     if answer not in answers:
    #         answers.append(answer)
    #     screen.update()

    if answer == "Exit":
        break
    elif answer in all_states:
        state_data = data[data.state == answer]
        x_cor = state_data.x.iloc[0]
        y_cor = state_data.y.iloc[0]
        answer_turtle.goto(x_cor, y_cor)
        answer_turtle.write(f"{answer}", True, align="center")
        if answer not in answers:
            answers.append(answer)
        screen.update()

    answer = screen.textinput(title=f"Next Guess {len(answers)}/50", prompt="Guess the next State: ").title()

    # if len(answers) == 50:
    #     game_on = False

# for state in all_states:
#     states_to_learn = []
#     if state not in answers:
#         states_to_learn.append(state)
#         pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv", index=False)

# List Comprehension
states_to_learn = [state for state in all_states if state not in answers]
pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv", index=False)

screen.exitonclick()
