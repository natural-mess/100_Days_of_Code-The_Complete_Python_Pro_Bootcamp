from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/6b78c3badded7def110f"

app = Flask(__name__)

@app.route('/')
def home():
    posts = get_blog_posts(BLOG_URL)
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

def get_blog_posts(url):
    response = requests.get(url=url, verify=False)
    response.raise_for_status()
    all_blog_posts = response.json()
    return all_blog_posts

@app.route('/post/<int:num>')
def get_blog(num):
    index=num-1
    posts = get_blog_posts(BLOG_URL)
    if index < len(posts):
        return render_template("post.html", post=posts[index])
    return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
    