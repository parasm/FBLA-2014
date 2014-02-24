from flask import Flask, render_template, request, session, redirect, escape
import jinja2
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():
	if request.method == "POST":
		return redirect('/thanks')
	return render_template("index.html")

@app.route('/thanks')
def thanks():
	return render_template("thanks.html")

@app.route('/blog')
def blog():
	return render_template("blog.html", blog=True)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)