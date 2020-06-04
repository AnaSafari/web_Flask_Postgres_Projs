from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

todoapp = Flask(__name__) ## names the application the name of the file
db = SQLAlchemy(todoapp)
todoapp.config['SQLALCHEMY_DATABASE_URI']='postgresql://Anahita@localhost:5432/todoapps'
todoapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Todo(db.Model):
	__tablename__ = "todos"
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable = False)

	def __repr__(self):
		return f'<Todo {self.id}{self.description}>'

task1 = Todo(id=1, description='Meeting with CTO')
task2 = Todo(id=2, description='Calling the Client')
task3 = Todo(id=3, description='Writing Code')
task4 = Todo(id=4, description='Having Lunch')

db.session.add_all([task1, task2, task3, task4])

db.create_all()

@todoapp.route('/')
def todoindex():
	return render_template('todoindex.html', data = Todo.query.all())


# if __name__ == '__main__':
# 	todoapp.run()
