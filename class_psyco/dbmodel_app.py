from flask import Flask
from flask_sqlalchemy import SQLAlchemy #a library we can link to our flask app and began using SQLalchemy

dbmodel_app = Flask(__name__)
db = SQLAlchemy(dbmodel_app) ## linking SQLAlchemy to flask app.  
							 ##This would link an instance of a database that we could interact within SQLAlchemy land to our flask app.
dbmodel_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Anahita@localhost:5432/foo' ## all configurations for connecting 
																							##the app to a database is set in a ##dictionary colled app_alchemy.config
																							
dbmodel_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
																									
class Person(db.Model):
	__tablename__ = 'persons' ## if not use __tablename__ , then tablename will be class name with lowercase																									
								## Usually for classes we need to initiate it, but SQLAlchemy initiates for us.
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(), nullable = False)

	def __repr__(self):
		return f'<Person ID: {self.id}, name: {self.name}>'



db.create_all()

@dbmodel_app.route('/')
def index():
	person = Person.query.first()
	return "Hello " + person.name

# In this case, @app.route is a Python decorator. 
# Decorators take functions and returns another function, 
# usually extending the input function with additional ("decorated") functionality. 
# @app.route is a decorator that takes an input function index() as the callback that gets invoked 
# when a request to route / comes in from a client.

if __name__ == '__main__':
	dbmodel_app.run() 

