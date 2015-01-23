import datetime
from Models import *

class Return(object):
  """docstring for Return"""

  def __init__(self):
    database.connect()

  def getDocumentURLs(self):
    "returns all document urls in the database"

    urls = []

    documents = Document.select().where(
      (Document.title == None) &
      (Document.text == None)
    )

    for document in documents:
      urls.append(document.url)

    return urls

  def getDocuments(self):
    "Returns all the text from the documents in the database"

    documents = []

    for document in Document.select():
      documents.append(document.text)

    return documents
