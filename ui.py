from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface(QuizBrain):
    def get_question(self):
        question = self.next_question()
        self.canvas.itemconfigure(self.screen_text, text=question)

    def check_for_true(self):
        if self.still_has_questions():
            answer = self.check_answer()
            if answer.lower() == 'true':
                self.score += 1
                self.label.config(text=f"Score: {self.score}")
                self.get_question()
            else:
                self.get_question()
        else:
            self.canvas.itemconfigure(self.screen_text,
                                      text=f"your score is: {self.score} out of {self.question_number}")

    def check_for_false(self):
        if self.still_has_questions():
            answer = self.check_answer()
            if answer.lower() == 'false':
                self.score += 1
                self.label.config(text=f"Score: {self.score}")
                self.get_question()
            else:
                self.get_question()
        else:
            self.canvas.itemconfigure(self.screen_text,
                                      text=f"your score is: {self.score} out of {self.question_number}")

    def __init__(self, q_list):
        super().__init__(q_list)
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas.grid(row=1, column=1, padx=(20, 20), pady=(40, 40), columnspan=5)
        self.canvas2 = Canvas(height=500, width=500, bg='white')
        self.q_text = self.next_question()
        self.screen_text = self.canvas.create_text(150, 125, text=self.q_text, width=250, font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR)
        self.yes_image = PhotoImage(file="./images/true.png")
        self.no_image = PhotoImage(file="./images/false.png")
        self.button_y = Button(image=self.yes_image, highlightthickness=0, command=self.check_for_true)
        self.button_y.grid(row=2, column=1, padx=20, pady=20)
        self.button_n = Button(image=self.no_image, highlightthickness=0, command=self.check_for_false)
        self.button_n.grid(row=2, column=5, padx=20, pady=20)
        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.label.grid(row=0, column=5, padx=20, pady=20)

        self.window.mainloop()
