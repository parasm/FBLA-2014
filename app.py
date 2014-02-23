from flask import Flask, render_template, request, session, redirect, escape
import jinja2
import os

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")
@app.route('/buy')
def buy():
	return render_template("buy.html")
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/blog')
def blog():
	return render_template("blog.html")

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)