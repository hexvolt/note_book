from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.config['MONGODB_SETTINGS'] = {
    'db': 'nb',
    'username': 'nb_admin',
    'password': '12345',
}

db = MongoEngine(app)

# registering blueprints
from note_book.views.core import core

app.register_blueprint(core)