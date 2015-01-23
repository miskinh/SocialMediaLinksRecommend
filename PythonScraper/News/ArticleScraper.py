"""
ArticleScraper.py uses newspaper to obtain the text from news articles
"""

#import shared functions
# from Shared import *

#import library functions
import os, re

from lxml import etree

#import newspaper article
from newspaper import Article

VERBOSE = True

class ArticleScraper():
  """
  ArticleScraper provides the framework to download and save the textual content of a news article
  """

  def __init__(self,language="en"):
    self.language = language
    self.article = None

  def getArticle(self,url):
    """
    setURL sets the article url
    """

    self.url = url
    self.article = Article(self.url,language=self.language)

    try:
      self.article.download()
      self.article.parse()
    except Exception as error:
      print(error)

    if VERBOSE: print self.article.title

    return self.article

  def printArticle(self):
    """
    printText prints the text contained within an article
    """

    print self.article.title
    print "=============="
    print self.article.text

  def saveArticle(self,folderName="",minLength=100):
    """
    saveArticle saves the textual content of the article within NewsArticles 
    folderName defined the sub directory where articles are stored
    """

    text = self.article.text
    if (len(text) < minLength): raise ValueError

    #join directory with folderName
    directory = os.path.join("SavedArticles",cleanFilename(folderName))

    #create directory if it does not exist
    if not os.path.exists(directory):
      os.makedirs(directory)

    #name the file the same as the web page title
    title = self.article.title
    fileName = "{}.txt".format(cleanFilename(title))
    filePath = os.path.join(directory,fileName)

    saveFile(filePath,text.encode('ascii','ignore'))

    return title,text

if (__name__ == "__main__"):
  articleScraper = ArticleScraper()

  articleScraper.getArticle('http://www.bbc.co.uk/news/world-asia-30706298')
  articleScraper.printArticle()
  articleScraper.saveArticle()

  articleScraper.getArticle('http://www.theguardian.com/lifeandstyle/wordofmouth/2015/jan/06/-sp-cup-soup-instant-taste-test-batchelors')
  articleScraper.saveArticle()

