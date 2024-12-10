from flask import Flask, render_template
import requests
import datetime
from post import Post  # Import the Post class

app = Flask(__name__)

# Function to get all blog posts from the API
def get_all_posts():
    """Fetches all blog posts from the npoint.io API and converts them to Post objects"""
    blog_url = "https://api.npoint.io/e7f09240c21f679be3b3"
    response = requests.get(blog_url)
    all_posts = response.json()
    # Convert each post dictionary into a Post object
    return [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_posts]

@app.route('/')
def home():
    """Home page route - displays all blog post previews"""
    posts = get_all_posts()
    current_year = datetime.datetime.now().year
    return render_template("index.html", posts=posts, current_year=current_year)

@app.route('/blog/<int:post_id>')
def show_post(post_id):
    """Individual blog post route - displays a single full blog post"""
    # Get all posts and find the one matching the requested ID
    posts = get_all_posts()
    requested_post = next((post for post in posts if post.id == post_id), None)
    current_year = datetime.datetime.now().year
    return render_template("post.html", post=requested_post, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)