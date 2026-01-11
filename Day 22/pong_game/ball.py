from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(x=0,y=0)
        self.move_speed = 0.05

        # Solution of using goto and change x and y coordinate
        # self.xdir = 5
        # self.ydir = 10

        # Solution of using setheading and change angles
        self.setheading(random.randrange(60, 300, 60))

    def move(self):
        # Solution of using goto and change x and y coordinate
        # self.goto(self.xcor()+self.xdir, self.ycor()+self.ydir)

        # Solution of using setheading and change angles
        self.forward(10)
    
    def bounce_wall(self):
        # In Turtle:
        # 0°   → right
        # 90°  → up
        # 180° → left
        # 270° → down
        # Angles go counter-clockwise, from 0 to 360.
        # When the ball hits top wall or bottom wall
        # The vertical direction must flip
        # The horizontal direction must stay the same
        # So:
        # x movement stays
        # y movement reverses
        # A bounce on a horizontal wall is a vertical mirror of the angle.
        # Mathematically, that mirror is: new_heading = 360 - old_heading
        # heading = 45°: ↗ 45°
        # Bounce on top wall → go down-right: ↘ 315°
        # 360 - 45 = 315
        self.setheading(360 - self.heading())

        # Another solution would be flipping y-coordinate, however, we would need 2 new attributes:
        # xdir and ydir
        # self.ydir *= -1

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_paddle()
