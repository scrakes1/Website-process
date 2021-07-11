from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def welcomepage():
    return "<p>Welcome to the Mountain Lion Computer Science Camp Python Course!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

"""@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f"hi"
    else:
        return f"cool"

with app.test_request_context():
    print(url_for('welcomepage'))
    print(url_for('hello', name=''))
    print(url_for('login'))
