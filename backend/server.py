from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(80))
    body    = db.Column(db.String(80))
    is_done = db.Column(db.Boolean())
    def __init__(self, title, body, is_done):
        self.title   = title
        self.body    = body
        self.is_done = is_done
    def __repr__(self):
        return '<User %r>' % self.title

db.create_all()

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/api/v1/add_random_todo', methods=["GET"])
def add_random_todo():
    new_todo = Todo("Title", "Body", False)
    db.session.add(new_todo)
    db.session.commit()
    return "added"

@app.route('/api/v1/todos', methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    results = []
    for todo in todos:
        results.append({
            'id'      : todo.id,
            'title'   : todo.title,
            'body'    : todo.body,
            'is_done' : todo.is_done
            })
    return jsonify(todos=results)

if __name__ == "__main__":
    app.run(debug=True)
