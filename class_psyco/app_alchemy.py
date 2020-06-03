from flask import Flask
from flask_sqlalchemy import SQLAlchemy #a library we can link to our flask app and began using SQLalchemy

app_alchemy = Flask(__name__)
db = SQLAlchemy(app_alchemy) ## linking SQLAlchemy to flask app.  
							 ##This would link an instance of a database that we could interact within SQLAlchemy land to our flask app.
app_alchemy.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Anahita@localhost:5432/foo' ## all configurations for connecting 
																									##the app to a database is set in a 
																									##dictionary colled app_alchemy.config

@app_alchemy.route('/')
def index():
	return "Hello World!"

# In this case, @app.route is a Python decorator. 
# Decorators take functions and returns another function, 
# usually extending the input function with additional ("decorated") functionality. 
# @app.route is a decorator that takes an input function index() as the callback that gets invoked 
# when a request to route / comes in from a client.

if __name__ == '__main__':
	app_alchemy.run() 