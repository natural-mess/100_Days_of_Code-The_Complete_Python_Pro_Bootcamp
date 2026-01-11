from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self, highest_score):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.update_scoreboard()
        self.game_control()

    def update_scoreboard(self):
        self.goto(0,270)
        self.check_highest_score()
        self.write(f"Score: {self.score} / (Highest: {self.highest_score})", move=False, align=ALIGNMENT,  font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.game_control()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT,  font=FONT)

    def game_control(self):
        self.goto(-270, -230)
        self.write(f"r: restart", move=False, align="left",  font=FONT)
        self.goto(-270, -250)
        self.write(f"c: pause", move=False, align="left",  font=FONT)
        self.goto(-270, -270)
        self.write(f"space: start / resume", move=False, align="left",  font=FONT)
        
    def check_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highest_score}")

