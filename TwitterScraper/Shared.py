"""
Shared.py contains shared functionality
"""

#library imports
import urllib2,HTMLParser

def loadFile(filename):
  "Load a file with the given filename and return the content of the file"

  with open(filename,"r") as openFile:
    content = openFile.read()

  return content

def saveFile(filename,content):
  "Save a file with the given filename and content"

  with open(filename,"w") as openFile:
    openFile.write(content)

def getURL(url):
  "Returns the content of the given URL and if there is an error raises"

  request = urllib2.Request(url,headers={'User-agent':'Mozilla'})

  try:
    response = urllib2.urlopen(request)
    content = response.read()
  except:
    content = ''

  return content

def parseHTML(html):
  "Returns a parsed version of the given HTML which is utf8 encoded"

  htmlParser = HTMLParser.HTMLParser()

  decodedHTML = html.decode("utf8")
  text = htmlParser.unescape(decodedHTML)

  return text