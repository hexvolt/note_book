import datetime
from note_book import db


class TimeStampedDocument(db.Document):
    created = db.DateTimeField(default=datetime.datetime.now, required=True)
    modified = db.DateTimeField()

    meta = {
        'abstract': True,
    }


class Post(TimeStampedDocument):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, unique=True)
    active = db.BooleanField(default=True)
    body = db.StringField()
    tags = db.ListField(
        db.StringField(max_length=100)
    )

    def __unicode__(self):
        return self.title

    meta = {
        'indexes': ['-created', 'slug'],
        'ordering': ['-created']
    }


class Chapter(TimeStampedDocument):
    title = db.StringField(max_length=255, required=True)
    order = db.IntField()
    active = db.BooleanField(default=True)
    posts = db.ListField(
        db.ReferenceField(Post, reverse_delete_rule=db.PULL)   # remove the references to deleted Post from this list
    )

    def __unicode__(self):
        return self.title

    meta = {
        'ordering': ['order']
    }


class User(db.EmbeddedDocument):
    name = db.StringField(max_length=100, required=True)
    email = db.EmailField(required=True)
    active = db.BooleanField(default=True)

    def __unicode__(self):
        return "{name} ({email})".format(name=self.name, email=self.email)

    meta = {
        'indexes': ['email'],
    }


class Comment(TimeStampedDocument):
    parent_post = db.ReferenceField(
        Post, reverse_delete_rule=db.CASCADE,    # delete all the Comments if a Post is deleted
        required=True
    )
    parent_comment = db.ReferenceField('self')
    author = db.EmbeddedDocumentField(User)
    body = db.StringField(required=True)

    def __unicode__(self):
        return "({user}): {comment}".format(user=self.author.email, comment=self.body)

    meta = {
        'indexes': ['parent_comment'],
        'ordering': ['-created']
    }