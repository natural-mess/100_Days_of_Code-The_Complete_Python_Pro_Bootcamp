from turtle import Turtle

FONT_LEVEL = ("Courier", 18, "normal")
FONT_CONTROL = ("Courier", 13, "normal")
FONT_INFO = ("Time New Roman", 24, "bold")
ALIGNMENT = "left"
FILE_PATH = "./data/level.txt"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        with open(FILE_PATH) as file:
            self.highest_level = int(file.read())
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.update_scoreboard()
        self.game_control()
    
    def update_scoreboard(self):
        """Show current level and highest level"""
        self.goto(-290,260)
        self.check_highest_level()
        self.write(f"Level: {self.level} / (Highest: {self.highest_level})", move=False, align=ALIGNMENT,  font=FONT_LEVEL)

    def increase_level(self):
        """Increase a level by 1"""
        self.level += 1
        self.clear()
        self.update_scoreboard()
        self.game_control()

    def game_control(self):
        """Show instruction for game control"""
        self.goto(-290, -270)
        self.write(f"q: quit", move=False, align=ALIGNMENT,  font=FONT_CONTROL)
        self.goto(-290, -290)
        self.write(f"space: pause / resume", move=False, align=ALIGNMENT,  font=FONT_CONTROL)

    def game_pause(self):
        """Show pause"""
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"PAUSE", move=False, align="center",  font=FONT_INFO)

    def game_resume(self):
        """After resuming from pause, show information again"""
        self.clear()
        self.color("green")
        self.update_scoreboard()
        self.game_control()

    def game_over(self):
        """Show gameover message"""
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", move=False, align="center",  font=FONT_INFO)
        self.goto(0, -20)
        self.color("red")
        self.write(f"(Click on the game window to exit)", move=False, align="center",  font=FONT_CONTROL)

    def check_highest_level(self):
        """Write highest level to file"""
        if self.level > self.highest_level:
            self.highest_level = self.level
            with open(FILE_PATH, "w") as file:
                file.write(f"{self.highest_level}")
