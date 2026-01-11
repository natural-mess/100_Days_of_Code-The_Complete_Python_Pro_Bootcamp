from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        (x, y) = coordinate
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x,y=y)
    
    def up(self):
        if self.ycor() < 250:
            self.goto(x=self.xcor(),y=self.ycor()+20)

    def down(self):
        if self.ycor() > -230:
            self.goto(x=self.xcor(),y=self.ycor()-20)

