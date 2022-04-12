from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_bizzy = QuizBrain(question_bank)

while quiz_bizzy.still_has_questions():
    quiz_bizzy.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz_bizzy.score}/{quiz_bizzy.question_number}.")
# new_question = Question(question_data[0]["text"], question_data[0]["answer"])
# print(new_question.text, new_question.answer)