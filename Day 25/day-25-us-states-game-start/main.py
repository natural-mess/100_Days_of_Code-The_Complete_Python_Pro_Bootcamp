import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
total_state = data.size

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

def get_user_input(title_info):
    """Get input from user"""
    answer_state = screen.textinput(title=title_info, prompt="What's another state's name?")

    if answer_state is not None:
        # Convert input to Title case
        answer_state = answer_state.title()
    
    return answer_state

score = 0
title_info = "Guess the State"
corrected_guess = []

# def get_mouse_click_coor(x, y):
#     """Callback function when user click on a position on image"""
#     global score, title_info

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

def export_not_guessed_states(corrected_guess):
    """Export the not guessed states in states_to_learn.csv"""
    not_guessed = data[~data["state"].isin(corrected_guess)]
    not_guessed.to_csv("states_to_learn.csv")

while True:
    # Get input from user
    answer_state = get_user_input(title_info)

    # User clicked Cancel or type exit
    if answer_state is None or answer_state == "Exit":
        t.color("red")
        t.goto(0, 0)
        t.write("GAME OVER", False, align='CENTER', font=('Arial', 20, 'bold'))
        t.color("blue")
        t.goto(0, -30)
        t.write("Click on screen to exit", False, align='CENTER', font=('Arial', 15, 'normal'))
        export_not_guessed_states(corrected_guess)
        break

    # Get the row in the data which contains the answer_state
    row = data[data["state"] == answer_state]
    if row.empty:
        title_info = f"Incorrected guess - {score}/{total_state} States Correct"
        continue
    
    # Check if the state has already been guessed before
    if row["state"].iloc[0] not in corrected_guess:
        score += 1
        title_info = f"{score}/{total_state} States Correct"
        corrected_guess.append(row["state"].iloc[0])
        t.goto(row["x"].iloc[0], row["y"].iloc[0])
        t.write(f"{answer_state}", False, align='left', font=('Arial', 8, 'normal'))
    else:
        title_info = f"Already guessed - {score}/{total_state} States Correct"

screen.exitonclick()