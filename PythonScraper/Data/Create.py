import datetime
from Models import *

class Create(object):
  """docstring for Create"""

  def __init__(self):
    database.connect()

  def addUserObject(self,user):
    "adds a user object"

    self.addUser(
      userName = user["userName"],
      followerUserNames=user["followers"],
      friendUserNames=user["friends"],
      postURLs=user["postURLs"],
      likeURLs=user["likeURLs"]
      )

  def addUser(self,userName,friendUserNames=[],followerUserNames=[],postURLs=[],likeURLs=[]):
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
    for postURL in postURLs:
      self.addPost(userName,postURL)

    #Loop documentURLs and add
    for likeURL in likeURLs:
      self.addLike(userName,likeURL)

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
    "adds a post of a document to the database"

    user = self.addUser(userName)
    document = self.addDocument(documentURL)

    try:
      post = Posting.get(
        (Posting.document == document) &
        (Posting.user == user)
      )
    except DoesNotExist:
      post = Posting.create(document = document, user=user)

  def addLike(self,userName,documentURL):
    "adds a like of a ocument to the database"

    user = self.addUser(userName)
    document = self.addDocument(documentURL)

    try:
      like = Liking.get(
        (Liking.document == document) &
        (Liking.user == user)
      )
    except DoesNotExist:
      like = Liking.create(document = document, user=user)


if (__name__ == "__main__"):
  create = Create()
  create.addUser("henry",["henryFollow1","henryFollow2"],["henryURL1","henryURL2"])
  create.addUser("ian",["ianFollow1","ianFollow2"],["ianURL1","ianURL2"])
  create.addFollow("henry","ian")
  create.addPost("henry","ianURL1")
  database.close()
