from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.geometry("350x580")

        # Label
        self.score = self.label = Label(
            self.window,
            text="Score: 0",
            font=("Arial", 20),
            fg="white",
            bg=THEME_COLOR,
            padx=20,
            pady=20)
        self.label.grid(row=0, column=1)

        # Canvas Elements
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Placeholder",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_true)
        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def is_true(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.quiz.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

        