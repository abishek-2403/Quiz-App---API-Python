from tkinter import *
from quiz_brain import QuizBrain

BG_COLOR = 'Gray'


class Interface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz-brain - True/False")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        self.score_text = Label(text="Score: 0", font=("Algerian", 15, "bold"), fg="white", bg=BG_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=500, height=400, bg="white")
        self.question_text = self.canvas.create_text(250, 200, text="Question",
                                                     font=("Times new roman", 25, "bold"), width=480)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        right_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=right_image, highlightthickness=0,
                                  borderwidth=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0,
                                   borderwidth=0, command=self.false_clicked)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, fill="black")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,text="You have Successfully completed the Quiz",
                                   fill="black")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_clicked(self):
        answer = "True"
        if self.quiz.check_answer(answer):
            self.give_feedback("green")
        else:
            self.give_feedback("red")

    def false_clicked(self):
        answer = "False"
        if self.quiz.check_answer(answer):
            self.give_feedback("green")
        else:
            self.give_feedback("red")

    def give_feedback(self, color):
        self.canvas.config(bg=color)
        self.canvas.itemconfig(self.question_text, fill="white")
        self.score_text.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
