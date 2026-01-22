from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomodoro():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60
    if second == 0:
        second = "00"
    # < 10 makes more sense than using a range...
    #elif second in range(1, 10):
    elif second < 10:
        second = "0" + str(second)
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        pomodoro_gui.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
#GUI Setup
pomodoro_gui = Tk()
pomodoro_gui.title("Pomodoro")
pomodoro_gui.config(padx=100, pady=50, bg=YELLOW)

#Canvas Elements
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))

#TK Elements
timer_label = Label(bg=YELLOW, fg=GREEN, text="TIMER", font=(FONT_NAME, 35))
checkmark = Label(bg=YELLOW, fg=GREEN, text="✓")
start_button = Button(bg=YELLOW, text="START",  command=start_pomodoro, highlightthickness=0, highlightbackground=YELLOW)
reset_button = Button(text="RESET", command=reset_pomodoro, highlightthickness=0, highlightbackground=YELLOW)

#Grid Setup
timer_label.grid(column=2, row=0)
canvas.grid(column=2, row=1)
# checkmark.grid(column=2, row=5)
start_button.grid(column=1, row=4)
reset_button.grid(column=3, row=4)

pomodoro_gui.mainloop()
