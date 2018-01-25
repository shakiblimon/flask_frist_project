from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


@app.route('/')
def index():
    app.debug = True
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/article')
def article():
    return  render_template('article.html')

@app.route('/login' , methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/members')
def members():
    return "Memebers"

@app.route('/hello/<string:name>')
def hello(name):
    return render_template(
        'test.html')



@app.route('/members/<string:name>/')
def getMenber(name):
    return name


if __name__ == '__main__':
    app.run(debug = True)
