import datetime
from Models import *

class Create(object):
  """Create is used to add entities to the database as defined in Models.py"""

  def __init__(self):
    database.connect()

  def addUserObject(self,user):
    """Adds a User to the database along with user relations and post urls

    Parameters:
    user -- dictionary containing the following user parameters
      - userName
      - followers
      - friends
      - postURLs
      - likeURLs
    """

    self.addUser(
      userName = user["userName"],
      followerUserNames=user["followers"],
      friendUserNames=user["friends"],
      postURLs=user["postURLs"],
      likeURLs=user["likeURLs"]
      )

  def addUser(self,userName,friendUserNames=[],followerUserNames=[],postURLs=[],likeURLs=[]):
    """Adds a User to the database, depending on the optional parameters also adds
    friends, followers, posted content and liked content. For any existing item in the
    database relations will be added for the existing entity

    Parameters:
      userName - userName of the user being added
      friendUserNames - list of userNames of people being followed by the user
      followerUserNames - list of userNames of people following the given user 
      postURLs - list of URLs posted by the given user
      likeURLs - list of URLs where the user has liked the comment containing the URL

    Returns:
      user - a User object of the added user as defined in Models.py
    """

    #Check if user exists else create
    try:
      user = User.get(User.userName == userName)
    except DoesNotExist:
      user = User.create(userName = userName)

    #Loop followers and add relationships
    for followerUserName in followerUserNames:
      self.addFollow(followerUserName,userName)

    #Loop friends and add relationships
    for friendUserName in friendUserNames:
      self.addFollow(userName,friendUserName)

    #Loop postURLs and add
    for postURL in postURLs:
      self.addPost(userName,postURL)

    #Loop likeURLs and add
    for likeURL in likeURLs:
      self.addLike(userName,likeURL)

    return user

  def addFollow(self,fromUserName,toUserName):
    """Adds a follow relationship from a given user to another as defined by 
    their userName, if either user does not exist then new users are created.

    Parameters:
      fromUserName - the userName of the follower
      toUserName - the userName of the followed

    Returns:
      follow - a Following object for the relationship as defined in Models.py
    """

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
    """Adds a document with the given URL to the database, if a document with the
    given URL exists then the existing document is returned

    Parameters:
      documentURL - the URL of the document being added to the database

    Returns:
      document - a Document object as defined in Models.py
    """

    try:
      document = Document.select().where(Document.url == documentURL)[0]
    except IndexError:
      document = Document.create(url=documentURL)

    return document

  def addPost(self,userName,documentURL):
    """Adds a post relationship to the database where the given userName has posted
    the given URL, if the user or document does not exist then they are added to the
    database

    Parameters:
      userName - the userName of the user that posted the document
      documentURL - the URL that has been posted

    Returns:
      post - a Posting object that has been added to the database
    """

    user = self.addUser(userName)
    document = self.addDocument(documentURL)

    try:
      post = Posting.get(
        (Posting.document == document) &
        (Posting.user == user)
      )
    except DoesNotExist:
      post = Posting.create(document = document, user=user)

    return post

  def addLike(self,userName,documentURL):
    """Adds a like relationship to the database where the given userName has liked
    the given URL, if the user or document does not exist then they are added to the
    database

    Parameters:
      userName - the userName of the user that has done the liking
      documentURL - the URL that has been liked

    Returns:
      like - a Liking object that has been added to the database
    """

    user = self.addUser(userName)
    document = self.addDocument(documentURL)

    try:
      like = Liking.get(
        (Liking.document == document) &
        (Liking.user == user)
      )
    except DoesNotExist:
      like = Liking.create(document = document, user=user)

    return like


if (__name__ == "__main__"):
  create = Create()
  create.addUser("henry",["henryFollow1","henryFollow2"],["henryURL1","henryURL2"])
  create.addUser("ian",["ianFollow1","ianFollow2"],["ianURL1","ianURL2"])
  create.addFollow("henry","ian")
  create.addPost("henry","ianURL1")
  database.close()
