from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TOP_WALL = 280
BOTTOM_WALL = -280

PADDLE_DISTANCE = 63
R_PADDLE_BOUNDARY = 320
L_PADDLE_BOUNDARY = -320

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Python Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True

def exit_game():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(exit_game, "space")

# Central dashed line
dash_line = Turtle()
dash_line.pencolor("white")
dash_line.hideturtle()
dash_line.penup()
dash_line.setheading(270)
dash_line.backward(300)
dash_line.pensize(10)
 
for i in range(15):
    dash_line.pendown()
    dash_line.forward(20)
    dash_line.penup()
    dash_line.forward(20)

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top and botton walls
    if ball.ycor() >= TOP_WALL or ball.ycor() <= BOTTOM_WALL:
        ball.bounce_wall()

    # Detect collision with paddles
    # This game has a bug that since the forward step for ball is only 10
    # when the ball touches the edge of the paddle, it will bounce on the paddle
    # a few times before leaving the paddle completely.
    # This ball.setx will detect that once the ball touches the paddle, the ball is pushed away from the paddle.
    if ball.distance(r_paddle) < PADDLE_DISTANCE and ball.xcor() > R_PADDLE_BOUNDARY:
        ball.bounce_paddle()
        ball.setx(R_PADDLE_BOUNDARY - 5)

    if ball.distance(l_paddle) < PADDLE_DISTANCE and ball.xcor() < L_PADDLE_BOUNDARY:
        ball.bounce_paddle()
        ball.setx(L_PADDLE_BOUNDARY + 5)

    if ball.xcor() >= SCREEN_WIDTH / 2 + 30:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() <= -SCREEN_WIDTH / 2 - 30:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
