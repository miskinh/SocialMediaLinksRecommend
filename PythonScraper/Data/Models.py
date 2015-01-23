import datetime
from peewee import *

database = MySQLDatabase('SocialMedia', **{'host': 'localhost', 'password': 'nimandian10', 'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):

    userName = CharField()
    timeCreated = DateTimeField(null=True)
    timeDicovered = DateTimeField(default=datetime.datetime.now)
    location = CharField(null=True)

    class Meta:
        db_table = 'User'

class Document(BaseModel):

    url = CharField(null=True)
    title = CharField(null=True)
    text = TextField(null=True) 

    timeDicovered = DateTimeField(default=datetime.datetime.now)
    timeUpdated = DateTimeField(null=True)

    class Meta:
        db_table = 'Document'

class Posting(BaseModel):

    user = ForeignKeyField(User, related_name='poster', db_column='posterID')
    document = ForeignKeyField(Document, related_name='posted', db_column='postedID')

    time = DateTimeField(null=True)

    class Meta:
        db_table = 'Posting'

class Following(BaseModel):

    fromUser = ForeignKeyField(User, related_name='follower', db_column="followerID")
    toUser = ForeignKeyField(User, related_name='following', db_column="followingID")
    
    timeCreated = DateTimeField(null=True)
    timeDiscovered = DateTimeField(default=datetime.datetime.now)
    timeLastDiscovered = DateTimeField(default=datetime.datetime.now)
    isActive = BooleanField(default=True)

    class Meta:
        db_table = 'Following'

class Liking(BaseModel):

    user = ForeignKeyField(User, related_name='liker', db_column="likerID")
    document = ForeignKeyField(Document, related_name='liked', db_column="likedID")
    time = DateTimeField(null=True)

    class Meta:
        db_table = 'Liking'

if __name__ == "__main__":
    database.connect()
    database.create_tables([User,Document,Posting,Following,Liking])
    database.close()
