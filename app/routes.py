from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Syed Kazim Hussain'}
    posts = [
        {
            'author': {'username': 'Simon Sinek'},
            'book': 'Start With Why!'
        },
        {
            'author': {'username': 'Clayton Christensen'},
            'book': 'How will you measure your life'
        },
        {
            'author': {'username': 'Travis Bradberry'},
            'book': 'Emotional Intelligence 2.0'
        }
    ]
    return render_template('index.html', title='Home Page', user=user, posts=posts)
