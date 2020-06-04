from flask import Flask, render_template

app = Flask(__name__) ## names the application the name of the file

@app.route('/')
def index():
	return render_template('index.html', data = [{
		'description': 'To do 1'}, {
		'description': 'To do 2'}, {
		'description': 'To do 3'}
		])