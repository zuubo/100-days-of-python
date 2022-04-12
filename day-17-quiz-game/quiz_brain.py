class QuizBrain:

    def __init__(self, input_list):
        self.question_number = 0
        self.question_list = input_list
        self.score = 0

    def still_has_questions(self):
        """Returns true if there are still questions left"""
        return self.question_number < len(self.question_list)
        # you can do this instead of using an if statement, it will return true as long as the statement is true

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_number = self.question_number
        q_text = current_question.text
        user_answer = input(f"Q.{q_number}: {q_text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            print("You got it")
            self.score += 1
        else:
            print("nice try but no")
        print(f"The correct answer was: {q_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")
