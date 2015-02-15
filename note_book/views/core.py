from flask import Blueprint, render_template
from note_book.models import Chapter

core = Blueprint('core', __name__)

@core.route('/')
def home_page():
    # get a list of chapters
    chapters = Chapter.objects(active=True)
    return render_template("base.html", chapters=chapters)