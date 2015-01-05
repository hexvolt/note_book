from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# registering blueprints
from note_book.views.core import core

app.register_blueprint(core)