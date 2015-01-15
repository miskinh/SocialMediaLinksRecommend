import newspaper


def test():
  bbcPaper = newspaper.build('http://www.bbc.co.uk/news/')

  print(len(bbcPaper.articles))

  for article in bbcPaper.articles:
      print(article.url)

  return

  for category in bbcPaper.category_urls():
      print(category)


if (__name__ == "__main__"):
  test()