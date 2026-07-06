from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# Source: https://html5up.net/dimension
# Edit website from Chrome Developer Tool, using js in Console
# document.body.contentEditable=true