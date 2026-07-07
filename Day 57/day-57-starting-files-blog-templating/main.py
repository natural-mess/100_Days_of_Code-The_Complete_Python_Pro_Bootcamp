from flask import Flask, render_template
import requests
from post import Post

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

def get_blog_posts(url):
    response = requests.get(url=url)
    all_blog_posts = response.json()
    post_list = []
    for post in all_blog_posts:
        post_instance = Post(post['id'], post['title'], post['subtitle'], post['body'])
        post_list.append(post_instance)

    return post_list

@app.route('/')
def home():
    all_posts = get_blog_posts(BLOG_URL)
    return render_template("index.html", all_posts=all_posts)

@app.route('/blog/<int:num>')
def get_blog(num):
    all_posts = get_blog_posts(BLOG_URL)
    return render_template("blog.html", post_data=all_posts[num])

if __name__ == "__main__":
    app.run()
