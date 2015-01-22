from peewee import *

database = MySQLDatabase('SocialMedia', **{'host': 'localhost', 'password': 'nimandian10', 'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):

    userName = CharField()

    timeDicovered = DateTimeField()
    timeCreated = DateTimeField(null=True)
    location = CharField(null=True)

    class Meta:
        db_table = 'User'

class Document(BaseModel):

    sparseWords = TextField(null=True)
    text = TextField(null=True)
    topics = TextField(null=True)
    url = CharField(null=True)

    class Meta:
        db_table = 'Document'

class Posting(BaseModel):

    user = ForeignKeyField(User, related_name='poster')
    document = ForeignKeyField(Document, related_name='posted')

    time = DateTimeField(null=True)

    class Meta:
        db_table = 'Posting'
        indexes = (
            (('user', 'document'), False),
        )

class Following(BaseModel):

    fromUser = ForeignKeyField(User, related_name='follower')
    toUser = ForeignKeyField(User, related_name='following')
    
    timeFirst = DateTimeField()
    timeLast = DateTimeField()
    isActive = BooleanField()

    class Meta:
        db_table = 'Following'
        indexes = (
            (('fromUser', 'toUser'), False),
        )

class Liking(BaseModel):

    user = ForeignKeyField(User, related_name='liker')
    document = ForeignKeyField(Document, related_name='liked')
    time = DateTimeField(null=True)

    class Meta:
        db_table = 'Liking'
        indexes = (
            (('user', 'document'), False),
        )

if __name__ == "__main__":
    database.connect()
    database.create_tables()
