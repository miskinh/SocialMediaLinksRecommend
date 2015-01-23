from News.ArticleScraper import ArticleScraper
from Return import Return
from Update import Update

def updateLinks(minLength=100):
  "updates all links in the database"

  articleScraper = ArticleScraper()
  returnData = Return()
  updateData = Update()

  urls = returnData.getDocumentURLs()

  for url in urls:
    article = articleScraper.getURL(url)

    if (len(article.text) < minLength):
      updateData.removeLink(url)
    else:
      updateData.updateLink(url,article.title,article.text)


