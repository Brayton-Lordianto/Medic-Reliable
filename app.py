# open terminal. source .venv/bin/activate and run there

from flask import Flask, render_template, request, redirect, url_for
from auth_util import *

# instantiate the app
app = Flask(__name__)

# route for home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    print("\n\n", request.form, "\n\n")
    
    # testing purposes only
    print(list(get_db().find({})), "\n\n\n\n")
    
    username = request.form['fusername']
    password = request.form['fpassword']
    
    status, _ = signup(username, password)
    if not status: return redirect(url_for('failed_auth'))
    
    # testing purposes only
    print(get_db().find({}))
    
    # go to the dashboard/profile page
    return redirect(url_for('dashboard', username = username))

@app.route('/login', methods=['POST'])
def login_post():
    print("\n\n", request.form, "\n\n")
    
    # testing purposes only
    print(list(get_db().find({})), "\n\n\n\n")
    
    username = request.form['fusername']
    password = request.form['fpassword']
    
    status, rec = login(username, password)
    if not status: return redirect(url_for('failed_auth'))
    
    # testing purposes only
    print(get_db().find({}))
    
    # go to the dashboard/profile page
    return redirect(url_for('dashboard', username = username)) 

    
@app.route('/failed_auth')
def failed_auth():
    return render_template('failed_auth.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username = username)

# run programmatically
if __name__ == "__main__":
    app.run(debug = True)
    