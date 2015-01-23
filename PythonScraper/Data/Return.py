import datetime
from Models import *

class Return(object):
  """docstring for Return"""

  def __init__(self):
    database.connect()

  def getAllDocumentURLs():
    "returns all document urls in the database"

    urls = []

    for document in Document.select():
      urls.append(document.url)

    return urls

  def getAllDocuments():
    "Returns all the text from the documents in the database"

    documents = []

    for document in Document.select():
      documents.append(document.text)

    return documents