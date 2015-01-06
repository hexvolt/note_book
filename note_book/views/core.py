from flask import Blueprint
from note_book import db

core = Blueprint('core', __name__)

@core.route('/')
def home_page():
    return "Hello world"