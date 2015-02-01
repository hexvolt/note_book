from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = MongoEngine(app)

# linking the assets
from utils import assets

# registering blueprints
from note_book.views.core import core

app.register_blueprint(core)