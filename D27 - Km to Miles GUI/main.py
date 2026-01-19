from tkinter import *

window = Tk()
window.title("Km to Mile Converter")
window.config(padx=20, pady=20)

def km_to_miles():
    miles = float(km.get()) * 0.62137
    number_label.config(text=f"{miles}")

km = Entry(width=8)
km.grid(column=1, row=0)

km_label = Label(window, text="Km")
km_label.grid(column=2, row= 0)

is_equal_to_label = Label(window, text="is equal to")
is_equal_to_label.grid(column=0, row= 1)

number_label = Label(window, text="0")
number_label.grid(column=1, row= 2)

measurement_label = Label(window, text="Miles")
measurement_label.grid(column=2, row= 2)

calculate_button = Button(text="Calculate", command=km_to_miles)
calculate_button.grid(column=1, row=3)

window.mainloop()
