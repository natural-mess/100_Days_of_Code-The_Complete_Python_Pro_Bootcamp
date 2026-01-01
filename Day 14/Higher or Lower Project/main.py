import art, game_data
import random

def printInfo(data1, data2):
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}")
    print(f"{art.vs}")
    print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}")
    userInput = input("Who has more followers, Type \'A\' or \'B\': ").lower()
    return userInput

def compare(data1, data2):
    if data1['follower_count'] > data2['follower_count']:
        return 'a'
    else:
        return 'b'

def game_play():
    game_over = False
    score = 0
    data2 = random.choice(game_data.data)
    while not game_over:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        data1 = data2
        data2 = random.choice(game_data.data)
        if data2 == data1:
            data2 = random.choice(game_data.data)
        userInput = printInfo(data1, data2)
        compareRes = compare(data1, data2)

        if userInput == compareRes:
            score += 1
            if compareRes == 'a':
                data2 = data1
        else:
            game_over = True

    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

game_play()

