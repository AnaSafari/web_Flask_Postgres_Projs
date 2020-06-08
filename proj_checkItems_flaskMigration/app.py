from flask import Flask, render_template, request, redirect, url_for
from flask_mobility import Mobility
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) ## names the application the name of the file
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://Anahita@localhost:5432/todoapps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

class Todo(db.Model):
	__tablename__ = "todos"
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable = False)
	completed = db.Column(db.Boolean, nullable = True)


	def __repr__(self):
		return f'<Todo {self.id}{self.description}{self.completed}>'



# task1 = Todo(id=1, description='Meeting with CTO')
# task2 = Todo(id=2, description='Calling the Client')
# task3 = Todo(id=3, description='Writing Code')
# task4 = Todo(id=4, description='Having Lunch')

# db.session.add_all([task1, task2, task3, task4])

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
	description = request.form.get('description', '')
	todo = Todo(description = description)
	db.session.add(todo)
	db.session.commit()
	return redirect(url_for('todoindex'))


@app.route('/')
def todoindex():
	return render_template('todoindex.html', data = Todo.query.all())


if __name__ == '__main__':
	app.run()
