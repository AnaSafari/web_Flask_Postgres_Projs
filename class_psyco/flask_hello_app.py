from flask import Flask

flask_hello_app = Flask(__name__)

@flask_hello_app.route('/')
def index():
	return "Hello World!"

# In this case, @app.route is a Python decorator. 
# Decorators take functions and returns another function, 
# usually extending the input function with additional ("decorated") functionality. 
# @app.route is a decorator that takes an input function index() as the callback that gets invoked 
# when a request to route / comes in from a client.

if __name__ == '__main__':
	flask_hello_app.run()