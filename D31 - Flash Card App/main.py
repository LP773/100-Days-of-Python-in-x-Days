from tkinter import *
import pandas as pd
import random
from pathlib import Path

from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"

file = "./data/words_to_learn.csv"
if Path(file).is_file():
    try:
        df = pd.read_csv(file)

        if df.empty:
            raise ValueError("No rows left")
    except (EmptyDataError, ValueError):
        df = pd.read_csv("./data/french_words.csv")
else:
    df = pd.read_csv("./data/french_words.csv")
to_learn = df.to_dict(orient="records")
current_card = {}

'''
My solution that may have complicated things
I'd like to potentially revisit and see if I can make it the program work with my original solution
'''
# french_to_english = {row["French"]: row["English"] for row in output}


def new_card():
    global current_card, flip_timer
    flashy.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image=flash_card_front)
    canvas.itemconfig(card_language, text=f"French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card["French"]}", fill="black")
    flip_timer = flashy.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card, image=flash_card_back)
    canvas.itemconfig(card_language, text=f"English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card["English"]}", fill="white")

def known():
    global current_card
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=FALSE)
    new_card()

    '''
    In order to progress I'm going to watch the walkthrough and comment out
    my attempt at trying to figure out how to use drop dataframes and create a new csv with known words
    From what I'm seeing, I was overthinking/overengineering the solution
    '''
    # test_card = df.sample().iloc[0]
    # print(test_card["French"], test_card["English"], test_card.name)
    # new_df = df.drop(test_card.index)
    # pd.write_csv("known_words.csv", new_df)


flashy = Tk()
flashy.title("Flashy")
flashy.config(bg=BACKGROUND_COLOR, width=800, height=526, padx=50, pady=50)

flip_timer = flashy.after(3000, func=flip_card)

# Images
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")
flash_card_front = PhotoImage(file="./images/card_front.png")
flash_card_back = PhotoImage(file="./images/card_back.png")

# Canvas (Flash Card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(0,0, image=flash_card_front, anchor="nw")
card_language = canvas.create_text(400, 150, text=f"", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text=f"", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_button = Button(image=correct_image, highlightthickness=0, command=known)
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=new_card)
incorrect_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

new_card()

flashy.mainloop()
