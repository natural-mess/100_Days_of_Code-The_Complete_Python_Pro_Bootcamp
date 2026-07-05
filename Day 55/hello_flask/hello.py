from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmVmcGM4MGdyMDhvdXY1amRzd3NmeGVlMzA0MGVseDRrYnJueW1tNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3owzW9t7Fgt7JiFHfW/giphy.gif" width=200px>')

def make_bold(func):
    def wrapper():
        return "<b>"+func()+"</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>"+func()+"</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>"+func()+"</u>"
    return wrapper

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello {name}, you are {number}</p>"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
