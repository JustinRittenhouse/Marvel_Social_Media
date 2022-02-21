from flask import flash, redirect, render_template, current_app, request, url_for
from flask_login import current_user
from app import db

from app.blueprints.collection.models import Character
from .import bp as app

@app.route('/')
def add():
    return render_template('collection/add.html')