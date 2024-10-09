class QuizBrain:
    def __init__(self,question_list ):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} [False/True] :")
        self.check_answer(current_question.answer, user_answer)
        

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower() :
            print("You got it ")
            self.score += 1 
        else:
            print("wrong answer")
        print(f"The correct answer is {correct_answer} ") 
        print(f"Your Score is {self.score}/{self.question_number}")
        print('\n')
    def last_score(self):    
        print("[+] You've completed the quiz")
        print(f"Your final score was {self.score}/{self.question_number}")
        