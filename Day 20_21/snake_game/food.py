from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.refresh()

    def refresh(self):
        # Angela uses randint(-280,280), but randrange(-280, 280, 20) makes the food
        # appears in the center of the snake since the snake's head is 20x20
        self.goto(random.randrange(-280, 281, 20), random.randrange(-280, 281, 20))