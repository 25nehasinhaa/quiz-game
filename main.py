from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] #list of question objects, under the question bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    #positional parameters below
    #new_qutesion variable created from Question class, with two parameters
    #Question(question_text, question_answer) - new object created
    new_question = Question(question_text, question_answer)
    #add to the question bank, each of the new questions created in the for loop
    question_bank.append(new_question)
#converting each piece of data from question_model with string key into
# an object, for an easy access of text and answer

#create our new quiz, new quizbrain object and when we initialise it
#we pass a list of questions
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():#if quiz still has questions remaining:
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")