import art, game_data
import random

def getData():
    get2Data = random.sample(game_data.data, 2)
    return get2Data

def printInfo(dataToCompare):
    print(f"Compare A: {dataToCompare[0]['name']}, a {dataToCompare[0]['description']}, from {dataToCompare[0]['country']}")
    print(f"{art.vs}")
    print(f"Against B: {dataToCompare[1]['name']}, a {dataToCompare[1]['description']}, from {dataToCompare[1]['country']}")
    userInput = input("Who has more followers, Type \'A\' or \'B\': ").lower()
    return userInput

def compare(dataToCompare):
    if dataToCompare[0]['follower_count'] > dataToCompare[1]['follower_count']:
        return 'a'
    else:
        return 'b'

def game_play():
    game_over = False
    score = 0
    while not game_over:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        genData = getData()
        userInput = printInfo(genData)
        compareRes = compare(genData)

        if userInput == compareRes:
            score += 1
        else:
            game_over = True

    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

game_play()

