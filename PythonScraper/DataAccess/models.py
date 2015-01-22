from peewee import *

database = MySQLDatabase('SocialMedia', **{'host': 'localhost', 'password': 'nimandian10', 'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Documentcontents(BaseModel):
    documentid = BigIntegerField(db_column='documentID', primary_key=True)
    sparsewords = TextField(db_column='sparseWords', null=True)
    text = TextField(null=True)
    topics = TextField(null=True)
    url = CharField(null=True)

    class Meta:
        db_table = 'DocumentContents'

class Userfollowing(BaseModel):
    followingid = BigIntegerField(db_column='followingID')
    followingname = CharField(db_column='followingName', null=True)
    isactive = IntegerField(db_column='isActive', null=True)
    timefirst = DateTimeField(db_column='timeFirst')
    timelast = DateTimeField(db_column='timeLast')
    userid = BigIntegerField(db_column='userID', primary_key=True)
    username = CharField(db_column='userName', null=True)

    class Meta:
        db_table = 'UserFollowing'

class Userposting(BaseModel):
    documentid = BigIntegerField(db_column='documentID', null=True)
    time = DateTimeField()
    url = CharField(null=True)
    userid = BigIntegerField(db_column='userID', primary_key=True)
    username = CharField(db_column='userName')

    class Meta:
        db_table = 'UserPosting'

class Users(BaseModel):
    userid = BigIntegerField(db_column='userID', primary_key=True)
    username = CharField(db_column='userName', null=True)

    class Meta:
        db_table = 'Users'

