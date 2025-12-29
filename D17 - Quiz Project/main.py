from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = Quiz(question_bank)
while quiz.still_has_question():
    quiz.next_question()

# score, question_number = quiz.finale()
print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
