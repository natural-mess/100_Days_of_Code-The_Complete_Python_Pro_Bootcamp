from flask import Flask, render_template
import random
from datetime import datetime
import requests

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    input_name = name.title()
    response_agify = requests.get(url=AGIFY_URL+f"?name={name}")
    response_agify.raise_for_status()
    age = response_agify.json()["age"]

    response_genderize = requests.get(url=GENDERIZE_URL+f"?name={name}")
    response_genderize.raise_for_status()
    gender = response_genderize.json()["gender"]

    return render_template('guess.html', name=input_name, age=age, gender=gender)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


