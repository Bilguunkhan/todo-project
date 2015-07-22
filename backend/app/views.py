
from flask import flash, redirect, session, url_for, request, g
from app import app, lm

@app.route('/api/v1.0/todos', methods=['GET'])
def index():
    return redirect(url_for('/api/v1.0/todos'))

