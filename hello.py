
from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
	            return '<p>Welcome!</p><a href="/about">About</a> <a href="/contact">Contact</a>'

@app.route('/about')
def about():
	return '<p>This application is running on the Flask web framework.</p><a href="https://flask.palletsprojects.com/">Visit Flask</a>'

@app.route('/contact')
def contact():
    return '<p>Contact me at: c24528663@mytudublin.ie</p>'
