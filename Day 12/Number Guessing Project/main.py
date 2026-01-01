import random
import art

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

def game_init():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")

def chooseLevel():
    select_level = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
    if select_level != "hard":
        attempt = EASY_ATTEMPT
    else:
        attempt = HARD_ATTEMPT
    return attempt

def game_play():
    game_init()
    attempt = chooseLevel()
    answer = random.randint(1, 100)
    while attempt:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt -= 1
        if guess < answer:
            print("Too low.")
            print("Guess again.")
        elif guess > answer:
            print("Too high.")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {answer}.")
            break
    if attempt == 0:
        print("You've run out of guesses.")

while input("Do you want to play a game of Number Guessing? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game_play()


