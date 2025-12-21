import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

graphic = [rock, paper, scissors]

choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
if choice < 0 or choice > 2:
    print("Your choice is out of range")
    exit()
else:
    print(graphic[choice])
# print(choice)

computer_choice = random.randint(0,len(graphic)-1)
print(f"Computer chose: \n{graphic[computer_choice]}")
# print(computer_choice)

result = ["Draw!", "You win!", "You lose!"]

# If choice and computer_choice are same, then choice-computer_choice = 0
# If choice > computer_choice
#   If choice == paper, then computer_choice must be rock, so choice-computer_choice = 1-0=1, result[1] = "You win!"
#   If choice == scissors, then if computer_choice == rock, so choice-computer_choice = 2-0=2, result[2] = "You lose!"
#   If choice == scissors, then if computer_choice == paper, so choice-computer_choice = 2-1=1, result[1] = "You win!"
# If choice < computer_choice
#   If computer_choice == paper, then choice must be rock, so choice-computer_choice = 0-1=-1, result[-1] = "You lose!"
#   If computer_choice == scissors, then if choice == rock, so choice-computer_choice = 0-2=-2, result[-2] = "You win!"
#   If computer_choice == scissors, then if choice == paper, so choice-computer_choice = 1-2=-1, result[-1] = "You lose!"
print(result[choice-computer_choice])