from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

timer = ""
word = {}
# ---------------------------- FLIP CARD ------------------------------ #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=f"{word['English']}", fill="white")

# ---------------------------- FRONT CARD WORDS ------------------------------- #
# Read data from csv
try:
    data_dict = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_dict = pd.read_csv("data/french_words.csv")
# Convert dataframe to list like [{column -> value}, … , {column -> value}]
dictionary_list = data_dict.to_dict(orient='records')
print(dictionary_list)

def generate_word():
    """Generate a random word from dictionary list"""
    global timer, word
    if timer:
        window.after_cancel(timer)
    word = random.choice(dictionary_list)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=f"{word['French']}", fill="black")

    timer = window.after(3000, flip_card)

def learned_word():
    dictionary_list.remove(word)
    print(len(dictionary_list))
    generate_word()

# ---------------------------- UPDATE DICTIONARY ON CLOSE ------------------------------- #
def is_saved():
    if messagebox.askyesno(title="Goodbye", message="Update dictionary based on this session?"):
        data = pd.DataFrame(dictionary_list)
        data.to_csv("data/words_to_learn.csv", index=False)
    window.destroy()

# ---------------------------- UI SETUP ------------------------------- #
# Window config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.protocol("WM_DELETE_WINDOW", is_saved)

# Canvas images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

# Canvas text
title_canvas = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Button
wrong_button = Button(image=wrong, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, bd=0,
                      activebackground=BACKGROUND_COLOR, command=generate_word)
right_button = Button(image=right, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, bd=0,
                      activebackground=BACKGROUND_COLOR, command=learned_word)

# Grid layout
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

# Generate new word at the very first time we launch program
generate_word()

window.mainloop()