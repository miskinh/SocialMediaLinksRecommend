import datetime
from Models import *

class Create(object):
  """docstring for Create"""

  def __init__(self):
    database.connect()

  def addUser(self,userName,friendUserNames=[],followerUserNames=[],documentURLs=[]):
    "add user adds the given user to the database"

    #Check if user exists else create
    try:
      user = User.get(User.userName == userName)
    except DoesNotExist:
      user = User.create(userName = userName)

    #Loop followers and add relationships
    for followerUserName in followerUserNames:
      self.addFollow(followerUserName,userName)

    #Loop followers and add relationships
    for friendUserName in friendUserNames:
      self.addFollow(userName,friendUserName)

    #Loop documentURLs and add
    for documentURL in documentURLs:
      self.addPost(userName,documentURL)

    return user

  def addFollow(self,fromUserName,toUserName):
    "adds a following relationship between two user "

    fromUser = self.addUser(fromUserName)
    toUser = self.addUser(toUserName)

    try:
      follow = Following.select().where(
        (Following.fromUser == fromUser) &
        (Following.toUser == toUser) &
        (Following.isActive == True)
        )[0]
    except IndexError:
      follow = Following.create(fromUser=fromUser,toUser=toUser)

    follow.timeLastDicovered = datetime.datetime.now()
    follow.save()

    return follow

  def addDocument(self,documentURL):
    "adds a document to the database"

    try:
      document = Document.select().where(Document.url == documentURL)[0]
    except IndexError:
      document = Document.create(url=documentURL)

    return document

  def addPost(self,userName,documentURL):
    "adds a post of a ocument to the database"

    user = self.addUser(userName)
    document = self.addDocument(documentURL)

    try:
      post = Posting.select().where(
        (Posting.document == document) &
        (Posting.user == user)
      )[0]
    except IndexError:
      post = Posting.create(document = document, user=user)


if (__name__ == "__main__"):
  create = Create()
  create.addUser("henry",["henryFollow1","henryFollow2"],["henryURL1","henryURL2"])
  create.addUser("ian",["ianFollow1","ianFollow2"],["ianURL1","ianURL2"])
  create.addFollow("henry","ian")
  create.addPost("henry","ianURL1")
  database.close()
