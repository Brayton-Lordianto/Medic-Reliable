from urllib import request
# open terminal. source .venv/bin/activate and run there

from flask import Flask, render_template, request

# instantiate the app
app = Flask(__name__)

# route for home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

# run programmatically
if __name__ == "__main__":
    app.run(debug = True)
    