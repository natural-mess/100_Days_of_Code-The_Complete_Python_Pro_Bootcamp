import random
from turtle import Turtle, Screen, TK

is_race_on = False
screen = Screen()
screen.setup(width=500, height=744)
screen.title("Turtle Race Game")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = None
turtle_list = []
pos_y= [-325, -201, -72, 58, 191, 325]

def game_init(colors):
    pos_y_index = 0
    screen.bgpic('images/racetrack-500x744.png')
    while True:
        user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? \n{colors}\nEnter a color or Cancel to exit: ")
        if user_bet == None:
            exit()
        elif user_bet not in colors:
            TK.messagebox.showinfo(title="Make your bet", message="Invalid choice, try again!")
        else:
            break
    
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-240, y=pos_y[pos_y_index])
        turtle_list.append(new_turtle)
        pos_y_index += 1
    return turtle_list, user_bet

turtle_list, user_bet = game_init(colors)

if user_bet:
    is_race_on = True
    
while is_race_on:
    # shuffle the turtle_list to avoid high winning probability of the first turtle
    random.shuffle(turtle_list)
    for turtle in turtle_list:
        if turtle.xcor() > 175:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                # print(f"You've won! The {winning_color} turtle is the winner!")
                TK.messagebox.showinfo(title="Race result", message=f"You've won! The {winning_color} turtle is the winner!")
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                TK.messagebox.showinfo(title="Race result", message=f"You've lost! The {winning_color} turtle is the winner!")
            
            res=TK.messagebox.askquestion('Exit Game', 'Do you want to play again? ')
            if res == 'yes':
                is_race_on = True
                screen.clearscreen()
                screen.bgpic('images/racetrack-500x744.png')
                turtle_list.clear()
                turtle_list, user_bet = game_init(colors)
            break # break for loop
        turtle.forward(random.randint(0, 10))

screen.exitonclick()