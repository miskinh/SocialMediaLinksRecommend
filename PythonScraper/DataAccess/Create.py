import datetime
from DataAccess.Models import *

class Create(object):
  """docstring for Create"""

  def __init__(self):
    database.connect()

  def addUser(self,userName,followerUserNames=[],documentURLs=[]):
    "add user adds the given user to the database"

    #Check if user exists else create
    try:
      user = User.get(User.userName == userName)
    except DoesNotExist:
      user = User.create(userName = userName)

    #Loop followers and add relationships
    for followerUserName in followerUserNames:
      self.addFollow(userName,followerUserName)

    #Loop documentURLs and add
    for documentURL in documentURLs:
      self.addDocument(documentURL)

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
    except DoesNotExist:
      follow = Following.create(fromUser=fromUser,toUser=toUser)

    follow.timeLastDicovered = datetime.datetime.now()
    follow.save()

    return follow

  def addDocument(self,documentURL):
    "adds a document to the database"

    try:
      document = Document.select().where(Document.url == documentURL)[0]
    except DoesNotExist:
      document = Document.create(url=documentURL)

    return document

if (__name__ == "__main__"):
  create = Create()
  create.addUser("hpgmiskn",["miskinFollow1","miskinFollow2"],["miskinURL1","miskinURL2"])
  database.close()