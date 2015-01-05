from flask import Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def home_page():
    return "Hello world"