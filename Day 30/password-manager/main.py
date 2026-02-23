from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_list += [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    # password_final = ""
    # for char in password_list:
    #     password_final += char
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Callback function when Add button is clicked, website name and password will be stored in data.txt"""
    website = web_entry.get().title()
    username = user_entry.get().title()
    password = pass_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if not len(website) or not len(username) or not len(password):
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {username}\n"
                                                              f"Password: {password}.\n"
                                                              f"Is it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    # f.write(f"{website} | {username} | {password}\n")
                    #Reading old data
                    data = json.load(f)

            except FileNotFoundError, json.decoder.JSONDecodeError:
                data = new_data
            else:
                if website in data:
                    is_updated = messagebox.askyesno(title=f"Update {website}", message=f"There is already a password saved for {website}.\n"
                                                                                        f"Do you want to overwrite?")
                    if is_updated:
                        data[website] = new_data[website]
                else:
                    #Updating old data with new data
                    data.update(new_data)
            finally:
                with open("data.json", "w") as f:
                    #Saving updated data
                    json.dump(data, f, indent=4)
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get().title()
    try:
        with open("data.json", "r") as f:
            # f.write(f"{website} | {username} | {password}\n")
            # Reading old data
            data = json.load(f)
    except FileNotFoundError, json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data.keys():
            account = data.get(website)
            messagebox.showinfo(title=website, message=f"Email: {account['username']}\n"
                                    f"Password: {account['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
app_logo = PhotoImage(file="logo.png")
window.iconphoto(False, app_logo)
canvas.create_image(100, 100, image=app_logo)

# Label
web_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

# Entry
web_entry = Entry()
web_entry.focus()
user_entry = Entry()
user_entry.insert(0, "example@gmail.com")
pass_entry = Entry()

# Button
generate_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add", command=save)
search_btn = Button(text="Search", command=find_password)

# Grid layout
canvas.grid(column=1, row=0)
web_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
pass_label.grid(column=0, row=3)
web_entry.grid(column=1, row=1, sticky="ew")
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
pass_entry.grid(column=1, row=3, sticky="ew")
generate_btn.grid(column=2, row=3, sticky="ew")
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")
search_btn.grid(column=2, row=1, sticky="ew")

window.mainloop()