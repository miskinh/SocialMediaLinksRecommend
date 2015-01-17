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

  def downloadArticles(self, siteURL):
    "downloadArticles downloads all artiles for the given siteURL"

    if (siteURL not in self.articleURLs.keys()): self.searchSite(siteURL)

    minLength = 250
    self.articles[siteURL] = {}

    for articleURL in self.articleURLs[siteURL][:10]:
      #get the article and then download
      self.articleScraper.getArticle(articleURL)
      
      try:
        name,text = self.articleScraper.saveArticle(siteURL,minLength)
        self.articles[siteURL][name] = text
      except ValueError: continue

    print(self.articles[siteURL])
    return self.articles[siteURL]

if (__name__ == "__main__"):
  siteScraper = SiteScraper()
  siteScraper.downloadArticles('http://www.bbc.co.uk/news/')