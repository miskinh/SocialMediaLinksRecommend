import newspaper

from ArticleScraper import ArticleScraper

class SiteScraper(object):
  """SiteScraper downloads all the the documents from a"""

  def __init__(self, language="en"):
    self.language = language
    self.articleScraper = ArticleScraper(self.language)
    self.articleURLs = {}
    self.articles = {}

  def searchSite(self, siteURL):
    "searchSite downloads all the known articles for the given site"

    paper = newspaper.build(siteURL,language=self.language)
    
    self.articleURLs[siteURL] = []

    for article in paper.articles:
      self.articleURLs[siteURL].append(article.url)

  def printArticles(self, siteURL):
    "prints articles and keyowrds"

    if (siteURL not in self.articleURLs.keys()): self.searchSite(siteURL)

    for articleURL in self.articleURLs[siteURL]:
      article = self.articleScraper.getArticle(articleURL)

      print(articleURL)
      print(article.title)
      print(article.keywords)
      print('=============')


  def downloadArticles(self, siteURL):
    "downloadArticles downloads all artiles for the given siteURL"

    if (siteURL not in self.articleURLs.keys()): self.searchSite(siteURL)

    minLength = 250
    self.articles[siteURL] = {}

    for articleURL in self.articleURLs[siteURL]:
      #get the article and then download
      self.articleScraper.getArticle(articleURL)
      
      try:
        title,text = self.articleScraper.saveArticle(siteURL,minLength)
        self.articles[siteURL][title] = text
      except ValueError: continue

    print(self.articles[siteURL])
    return self.articles[siteURL]

if (__name__ == "__main__"):
  siteScraper = SiteScraper()
  siteScraper.printArticles('http://www.theguardian.com/uk')