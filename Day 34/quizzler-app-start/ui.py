from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window config
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas images
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        # set width to 280, which is a bit smaller than canvas width (300) to wrap text
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question", fill=THEME_COLOR, font=FONT
        )
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # Canvas text
        self.score = Label(text="Score: ", background=THEME_COLOR, fg="white")

        # Button
        self.true_btn = Button(
            image=true_img,
            highlightthickness=0,
            relief="flat",
            bd=0,
            activebackground=THEME_COLOR,
            command=self.true_command,
        )
        self.false_btn = Button(
            image=false_img,
            highlightthickness=0,
            relief="flat",
            bd=0,
            activebackground=THEME_COLOR,
            command=self.false_command,
        )

        # Grid layout
        self.score.grid(row=0, column=1, pady=(0, 20))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(30, 50))
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        # Get question and show it in canvas
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.true_btn.config(state="active")
            self.false_btn.config(state="active")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nFinal score: {self.quiz.score}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_command(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_command(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
