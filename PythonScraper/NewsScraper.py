from Shared import *
from NewsScraper.SiteScraper import SiteScraper
from OnlineLDA.onlineldavb import parse_doc_list

import os

def run(siteURL):

  siteScraper = SiteScraper()
  articles = siteScraper.downloadArticles(siteURL)
  print(articles)

  vocab = {}
  words = str.split(file("OnlineLDA/dictnostops.txt").read())
  for i,word in enumerate(words): vocab[word] = i

  for name,text in articles.items():
    (wordids, wordcts) = parse_doc_list([text],vocab)

    filecontent = [wordids[0],wordcts[0]]
    filename = os.path.join("SavedArticles",cleanFilename(siteURL),"{}.json".format(cleanFilename(name)))
    print(filename,filecontent)
    saveJSON(filename,filecontent)

if (__name__ == "__main__"):
  run('http://edition.cnn.com/')
  run('http://www.bbc.co.uk/news/')
  run('http://www.theguardian.com/uk')
  run('http://www.independent.co.uk/')
  run('http://www.thetimes.co.uk/tto/news/')