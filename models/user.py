
from mongoengine import StringField, EmailField, BooleanField, \
    Document, DateTimeField, IntField, SequenceField
from flask.ext.login import UserMixin
import datetime

class User(Document, UserMixin):
    username = StringField(max_length=200)
    password = StringField(max_length=200, default='')
    name = StringField(max_length=100)
    email = EmailField()
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    last_login = DateTimeField(default=datetime.datetime.now)
    skipped = IntField(default=0)
    processed = IntField(default=0)
    tags = SequenceField(default=[])

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.admin or False

