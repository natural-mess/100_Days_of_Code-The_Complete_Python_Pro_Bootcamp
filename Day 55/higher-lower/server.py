from flask import Flask
import random

result = random.randint(0, 9)
print(result)

app = Flask(__name__)

@app.route("/")
def intro():
    return ('<h1><b>Guess a number between 0 and 9</b></h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:num>")
def guessing_number(num):
    if num < result:
        return ('<h1 style="color:red;">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif num > result:
        return ('<h1 style="color:purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1 style="color:green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

if __name__ == "__main__":
    app.run()