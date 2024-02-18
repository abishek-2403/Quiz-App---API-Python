from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import Interface

question_list = []
for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    next_question = Question(question, answer)
    question_list.append(next_question)

quiz = QuizBrain(question_list)
quiz_interface = Interface(quiz)
