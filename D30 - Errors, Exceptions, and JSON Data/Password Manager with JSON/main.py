from calendar import day_abbr
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    combined_password = password_letters + password_symbols + password_numbers
    shuffle(combined_password)

    password = "".join(combined_password)
    if password_entry.get() != "":
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        password_entry.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showerror("Error", "Please make sure to have the inputs for the website and password fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        # Instructor's Solution wasn't working either. The JSONDecodeError needs to also be caught
        except FileNotFoundError, JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(f"{website}", f"Email: {data[website]["email"]}\n Password: {data[website]["password"]}")
    except KeyError:
        messagebox.showerror("Error", f"No details for the {website} exists.")
        website_entry.delete(0, END)

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
website_entry = Entry(width=21)
email_user_entry = Entry(width=38)
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1)
website_entry.focus()
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "test@email.com")
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=add_password)
search_button = Button(width=13, text="Search", command=search)

password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

pwd_manager.mainloop()
