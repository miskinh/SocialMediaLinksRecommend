import datetime
from Models import *
from Create import Create


class Update(Create):
  """docstring for Update"""

  def __init__(self):
    super(Update, self).__init__()

  def updateLink(self,url,title,text):
    "adds the link text to a database"

    document = self.addDocument(url)
    document.title = title
    document.text = text
    document.save()

  def removeLink(self,url):
    "removes the given url from the document table if no text title is set"

    documents = Document.select().where(
      (Document.url == url) &
      (Document.title == None) &
      (Document.text == None)
    )

    try:
      document = documents[0]
    except IndexError:
      print("No documents found for {}".format(url))
      return

    document.delete_instance(recursive=True)

  def removeFollow(self,fromUserName,toUserName):
    "specifies a follow relationship as no longer active"

    follow = self.getFollow(fromUserName,toUserName)
    follow.isActive = False
    sollow.save()
