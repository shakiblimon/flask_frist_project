from flask import Flask, flash, redirect, render_template, request, session, abort
from data import Articles

app = Flask(__name__)

Articles=Articles()

@app.route('/')
def index():
    app.debug = True
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles= Articles)

@app.route('/article/<string:id>/')
def article(id):
    return  render_template('article.html',id =id)

@app.route('/login' , methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return  render_template('register.html')

@app.route('/members')
def members():
    return "Memebers"


if __name__ == '__main__':
    app.run(debug = True)
