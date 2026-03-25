from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
pwd_manager = Tk()
pwd_manager.title("Password Manager")
pwd_manager.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
email_user_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entry Fields
website_entry = Entry(width=35)
email_user_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1, columnspan=2)
email_user_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36)

password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

pwd_manager.mainloop()
