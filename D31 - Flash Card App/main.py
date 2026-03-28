from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
french_to_english = {}
french_word = ""
english_word = ""

def read_csv():
    global french_to_english
    df = pd.read_csv("./data/french_words.csv")
    output = df.to_dict(orient="records")

    french_to_english = {row["French"]: row["English"] for row in output}
    return french_to_english

def new_card():
    global french_to_english, french_word, english_word, flip_timer
    flashy.after_cancel(flip_timer)
    french_word = random.choice(list(french_to_english.keys()))
    english_word = french_to_english[french_word]
    canvas.itemconfig(card, image=flash_card_front)
    canvas.itemconfig(card_language, text=f"French", fill="black")
    canvas.itemconfig(card_word, text=f"{french_word}", fill="black")
    flip_timer = flashy.after(3000, flip_card)

def flip_card():
    global french_to_english, french_word, english_word
    english_word = french_to_english[french_word]
    canvas.itemconfig(card, image=flash_card_back)
    canvas.itemconfig(card_language, text=f"English", fill="white")
    canvas.itemconfig(card_word, text=f"{english_word}", fill="white")

read_csv()

flashy = Tk()
flashy.title("Flashy")
flashy.config(bg=BACKGROUND_COLOR, width=800, height=526, padx=50, pady=50)

flip_timer = flashy.after(3000, flip_card)

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
correct_button = Button(image=correct_image, highlightthickness=0, command=new_card)
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=new_card)
incorrect_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

new_card()

flashy.mainloop()
