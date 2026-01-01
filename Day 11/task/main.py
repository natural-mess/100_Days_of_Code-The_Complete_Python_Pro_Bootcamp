import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Print cards and scores information
def print_Cards_Scores(userCards, computerCards, computerPos, final):
    if not final:
        print(f"    Your cards: {userCards}, current score: {sum(userCards)}")
        print(f"    Computer's first card: {computerCards[0]}")
    else:
        print(f"   Your final hand: {userCards}, final score: {sum(userCards)}")
        if computerPos == 0:
            print(f"   Computer's final hand: {computerCards[0]}, final score: {computerCards[0]}")
        else:
            print(f"   Computer's final hand: {computerCards}, final score: {sum(computerCards)}")

# Calculate user score and computer score and return corresponding value
# Return:
## True: Stop user from getting more cards
## False: User can continue if he/she wants
def calculateScore(cardList):
    score = sum(cardList)
    if score == 21:
        return True
    elif score < 21:
        return False
    else:
        # Check if there is ace and score is more than 21, then conver 11 to 1
        # Otherwise, return True
        if 11 in cardList:
            cardList.remove(11)
            cardList.append(1)
            return False
        else:
            return True

# Compare user's score vs computer score
## return 0: if equal
## return 1: list 1 wins
## return -1: list 2 wins
def compareScores(cardList1, cardList2):
    scoreList1 = sum(cardList1)
    scoreList2 = sum(cardList2)
    if scoreList2 > 21:
        return 1
    elif scoreList2 <= 21:
        if scoreList1 > scoreList2:
            return 1
        elif scoreList1 < scoreList2:
            return -1
        else:
            return 0

startGame = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")

while startGame != 'n':
    print(art.logo)
    userCards = random.sample(cards, 2)
    computerCards = random.sample(cards, 2)

    while not calculateScore(userCards):
        print_Cards_Scores(userCards, computerCards, computerPos=0, final=False)
        getNewCard = input("Type \'y\' to get another card, type \'n\' to pass: ")
        if getNewCard != 'n':
            userCards.append(random.choice(cards))
        else:
            break

    print_Cards_Scores(userCards, computerCards, computerPos=0, final=False)

    if sum(userCards) <= 21:
        while sum(computerCards) < 17:
            computerCards.append(random.choice(cards))
        print_Cards_Scores(userCards, computerCards, computerPos=1, final=True)
        result = compareScores(userCards, computerCards)
        if result == 0:
            print("Draw")
        elif result == -1:
            print("You lose")
        else:
            print("You win")
    else:
        print_Cards_Scores(userCards, computerCards, computerPos=0, final=True)
        print("You lose")

    startGame = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")

