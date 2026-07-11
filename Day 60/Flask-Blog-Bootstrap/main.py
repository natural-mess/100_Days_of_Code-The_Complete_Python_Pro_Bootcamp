from flask import Flask, render_template, request
import requests
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

BLOG_URL = "https://api.npoint.io/6b78c3badded7def110f"

ethereal_email = os.environ.get("ETHEREAL_EMAIL")
ethereal_password = os.environ.get("ETHEREAL_PASSWORD")
ethereal_host = os.environ.get("ETHEREAL_HOST")

app = Flask(__name__)


@app.route("/")
def home():
    posts = get_blog_posts(BLOG_URL)
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

# Ethereal cannot send email to another email, so here we send email to ourselves no matter what email user inputs
def send_emails(receiver_email, email_body):
    with smtplib.SMTP(ethereal_host, 587) as connection:
        connection.starttls()
        connection.login(ethereal_email, ethereal_password)
        connection.sendmail(
            from_addr=ethereal_email,
            to_addrs=ethereal_email,
            msg=f"Subject:Blog contact from {receiver_email}\n\n{email_body}".encode("utf-8"),
        )


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_emails(data["email"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


def get_blog_posts(url):
    response = requests.get(url=url, verify=False)
    response.raise_for_status()
    all_blog_posts = response.json()
    return all_blog_posts


@app.route("/post/<int:num>")
def get_blog(num):
    index = num - 1
    posts = get_blog_posts(BLOG_URL)
    if index < len(posts):
        return render_template("post.html", post=posts[index])
    return "Post not found", 404


if __name__ == "__main__":
    app.run(debug=True)
