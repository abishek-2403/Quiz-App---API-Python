import html


class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        if self.q_number < len(self.q_list):
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.q_list[self.q_number]
        self.q_number += 1
        formatted_question = html.unescape(self.current_question.question)
        return f"Q.NO.{self.q_number}: {formatted_question}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer.lower()
        if user_answer.lower() == correct_answer:
            self.score += 1
            return True

        else:
            return False
