"""
TwitterScraper.py uses TwitterURLs and ArticleScraper to save a number of twitter links to a minimised version in the SavedPages
"""

from NewsScraper.ArticleScraper import ArticleScraper
from TwitterScraper.TwitterURLs import TwitterURLs

def getTwitterURLs(userID='owner'):
  "gets all the urls in recent posts by the given user"

  twitterURLs = TwitterURLs()
  urls = twitterURLs.getURLs()

  return urls

def saveArticles(urls):
  "saves the paragraph content of all urls given"

  articleScraper = ArticleScraper()

  for url in urls:
    articleScraper.getArticle(url)
    articleScraper.saveArticle("Test")

def runSaveArticles(useTwitter=False):
  "saves the articles shared by owner or a sample set of articles defined bellow"
  #Change to false to not use twitter

  if useTwitter:
    urls = getTwitterURLs()
  else:
    urls = SAVED_URLS

  saveArticles(urls)

def getAllTwitterArticles():
  "saves the text content for all "

  twitterURLs = TwitterURLs(32)
  articleScraper = ArticleScraper()

  userURLs = twitterURLs.getAllURLs()

  for screenName,urls in userURLs.items():
    for url in urls:
      try:
        articleScraper.getArticle(url)
        articleScraper.saveArticle(screenName)
      except ValueError:
        continue

SAVED_URLS = [u'http://gizmo.do/CJSCp2P',
        u'http://bit.ly/1r1TeoM',
        u'http://bbc.in/1yDEHEl',
        u'http://off365.ms/JkASS7',
        u'http://bit.ly/1vlUiKe',
        u'http://asos.to/FashionFriendsy',
        u'http://bit.ly/1wyfAPX',
        u'http://ibm.co/13tzUe7',
        u'http://www.technologyreview.com/news/533526/new-form-of-memory-could-advance-brain-inspired-computers/',
        u'http://klou.tt/1r3voxepmrdjf',
        u'http://klou.tt/1mr1i4i1p9nt8',
        u'http://youtu.be/EGl2tYLzVLA',
        u'http://spoti.fi/1wjyGMT',
        u'http://tcrn.ch/1GcWLtd',
        u'http://klou.tt/uwuzf3ksyrlh',
        u'http://s.hbr.org/115ohsP']

if (__name__ == "__main__"):
  # runSaveArticles()
  getAllTwitterArticles()
