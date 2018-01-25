from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


@app.route('/')
def index():
    app.debug = True
    return render_template('test.html')

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
