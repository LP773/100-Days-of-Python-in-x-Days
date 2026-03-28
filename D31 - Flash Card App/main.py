from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

flashy = Tk()
flashy.title("Flashy")
flashy.config(bg=BACKGROUND_COLOR, width=800, height=526, padx=50, pady=50)

# Images
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")
flash_card_front = PhotoImage(file="./images/card_front.png")
flash_card_back = PhotoImage(file="./images/card_back.png")

# Canvas (Flash Card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(0,0, image=flash_card_front, anchor="nw")
canvas.create_text(400, 150, text="Sample", font=("Arial", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Sample", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_button = Button(image=correct_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
incorrect_button = Button(image=incorrect_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, relief='flat', bd=0)
incorrect_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)
flashy.mainloop()

