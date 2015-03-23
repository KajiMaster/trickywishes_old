# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, send_from_directory

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# my practice tab; loading the template into this as if root.
@app.route('/start')
def start():
    return render_template('index.html')  # render a template

# opening the images directory for template. Would use nginx to host these in production
@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
