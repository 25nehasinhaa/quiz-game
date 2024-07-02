class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self): #starts out being 0, and the  till the end
        return self.question_number < len(self.question_list)

    #we define a new method, called next_question, this method gets
    #hold of the current question, & that will be from question list (list of q from main.py) (question bank - each item inside that list is a question object having text and ans attributes)
    #then we tap into that list and get a hold of the item at the
    #current question number
    def next_question(self): #current question is a q object w text & ans attribute
        current_question = self.question_list[self.question_number] # we need a 0 here (question_num=0) in order to get hold of the 1st q from the list
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

