from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

todoapp = Flask(__name__) ## names the application the name of the file
db = SQLAlchemy(todoapp)
todoapp.config['SQLALCHEMY_DATABASE_URI']='postgresql://Anahita@localhost:5432/todoapp'
todoapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Todo(db.Model):
	__tablename__ = "todos"
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable = False)

	def __repr__(self):
		return f'<Todo {self.id}{self.description}>'

task1 = Todo(1, 'Meeting with CTO')
task2 = Todo(2, 'Calling the Client')
task3 = Todo(3, 'Writing Code')
task4 = Todo(4, 'Having Lunch')

todos.add(task1)

db.create_all()

@todoapp.route('/')
def todoindex():
	return render_template('todoindex.html', data = Todo.query.all())


if __name__ = '__main__':
	todoapp.run()