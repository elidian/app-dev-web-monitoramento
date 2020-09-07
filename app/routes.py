from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Elidian'}
    posts = [
        {
            'author': {'username': 'cam01'},
            'body': 'Hey!'
        },
        {
            'author': {'username': 'cam10'},
            'body': 'Hello!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)