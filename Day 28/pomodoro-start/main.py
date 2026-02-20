from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- FOCUS WINDOW ------------------------------- #
def focus_window(option):
    if option:
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    else:
        window.attributes('-topmost', 0)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # No need global timer because global is only required when you assign to a global variable inside a function — not when you only read/use it.
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    start_btn["state"] = "active"
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    start_btn["state"] = "disabled"
    focus_window(True)
    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short break", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=PINK)
    focus_window(False)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkmarks = ""
        for _ in range(math.floor(reps/2)):
            checkmarks += "✔"
        checkmark_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
window.iconphoto(False, tomato_img)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))

# Label
title_label = Label(text="Timer", width=11, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))

checkmark_label = Label(fg=GREEN, bg=YELLOW)

# Button
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)

# Grid layout
canvas.grid(column=1, row=1)
title_label.grid(column=1, row=0)
checkmark_label.grid(column=1, row=3)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

window.mainloop()