from flask import Blueprint, render_template
from note_book import db

core = Blueprint('core', __name__)

@core.route('/')
def home_page():
    return render_template("base.html")