import datetime
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
    "removes the given url from the document table"

    documents = Document.select().where(Document.url == url)

    if (len(documents) > 1):
      raise ValueError("Too many documents returned")
    elif (len(documents) < 1):
      raise ValueError("No documents with given url found")
    else:
      document = documents[0]

    document.delete_instance(recursive=False)

  def removeFollow(self,fromUserName,toUserName):
    "specifies a follow relationship as no longer active"

    follow = self.getFollow(fromUserName,toUserName)
    follow.isActive = False
    sollow.save()