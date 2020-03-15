from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/')
@app.route('/home.html')
def Home():
	return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
