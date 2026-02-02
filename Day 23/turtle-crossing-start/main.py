import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

game_is_pause = False
game_is_on = True

def pause_game():
    """Set or unset game_is_pause to pause or resume game"""
    global game_is_pause
    game_is_pause = not game_is_pause
    if game_is_pause:
        scoreboard.game_pause()
    else:
        scoreboard.game_resume()

def quit_game():
    """Unset game_is_on to stop the game completely"""
    global game_is_on
    game_is_on = not game_is_on
    scoreboard.game_over()

def car_player_collision_check(car, player):
    """Check collision between car and player"""
    for each_car in car.car_active:
        if player.ycor() > each_car.ycor() - 22 and player.ycor() < each_car.ycor() + 22:
            if each_car.distance(player) <= 40:
                return True
    return False

screen.listen()
screen.onkeypress(fun=pause_game, key="space")
screen.onkeypress(fun=quit_game, key="q")
screen.onkeypress(fun=player.move, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # If user presses space, game is pause
    if game_is_pause:
        continue

    car.car_spawn()
    car.car_move_reuse()

    # If there is collusion between player and car, stop the game completely
    if car_player_collision_check(car, player):
        quit_game()

    # If a level is completed
    if player.ycor() >= 280:
        scoreboard.increase_level()
        player.start_position()
        car.car_reset_level()

screen.exitonclick()