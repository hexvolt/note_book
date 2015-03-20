from flask import Blueprint, render_template, jsonify
from note_book.models import Chapter

core = Blueprint('core', __name__)

@core.route('/')
def home_page():
    # get a list of chapters
    chapters = Chapter.objects(active=True)
    return render_template("base.html", chapters=chapters)


@core.route('/articles/')
def get_articles():
    # returns a list of articles filtered by passed params
    articles = []
    for n in xrange(10):
        articles.append({
            "title": "Article %s" % n,
            "summary": "Lorem ipsum %s ..." % n
        })
    return jsonify(articles=articles)