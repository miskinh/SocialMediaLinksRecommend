from News.ArticleScraper import ArticleScraper
from Data.Return import Return
from Data.Update import Update

def updateLinks(minLength=100):
  "updates all links in the database"

  articleScraper = ArticleScraper()
  returnData = Return()
  updateData = Update()

  urls = returnData.getDocumentURLs()

  for url in urls:
    print url
    article = articleScraper.getArticle(url)
    if (len(article.text) < minLength):
      updateData.removeLink(url)      
    else:
      updateData.updateLink(url,article.title,article.text)


if (__name__ == "__main__"):
  updateLinks(200)
