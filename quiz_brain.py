# TODO: asking the question
# TODO: checking if the answer is correct
# TODO: checking if we are at the end of the quiz

class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.user_score =0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        text = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {text} (True/False)?: ")
        self.check_answer(user_ans, answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it Right!")
            self.user_score += 1
        else :
            print("Incorrect Answer.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is : {self.user_score}/{self.question_number}")
        print("\n")

    def get_final_score(self):
        return f"{self.user_score}/{self.question_number}"




