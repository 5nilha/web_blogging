from flask import Flask, render_template, request, session
from src.models.user import User
from src.common.database import Database

app = Flask(__name__)

app.secret_key = "ofoefiegfefighbhugduas[qewehkdfbcws"

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def hello_method():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run(port=4995, debug=True)