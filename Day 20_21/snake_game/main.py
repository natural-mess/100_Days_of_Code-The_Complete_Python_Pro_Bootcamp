from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

def pause_game():
    global game_is_on
    game_is_on = False

def resume_game():
    global game_is_on
    game_is_on = True

def restart():
    global game_restart
    game_restart = True

highest_score = 0

def game_init():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(highest_score)
    game_is_on = False
    game_restart = False
    
    screen.listen()
    # Angela uses onkey but here onkeypress means the button is taken into account once key is pressed
    # onkey will have affect when key is released
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(resume_game, "space")
    screen.onkeypress(pause_game, "c")
    screen.onkeypress(restart, "r")
    return screen, snake, food, scoreboard, game_is_on, game_restart

screen, snake, food, scoreboard, game_is_on, game_restart = game_init()

while True:
    screen.update()
    time.sleep(0.1)

    if game_is_on: 
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    if game_restart:
        highest_score = scoreboard.highest_score
        screen.reset()
        screen, snake, food, scoreboard, game_is_on, game_restart = game_init()

screen.exitonclick()
