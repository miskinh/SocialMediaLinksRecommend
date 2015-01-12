"""
DocumentScraper.py is used to obtain the core text from a web page to enable assessment of the topic of the page
"""

#import shared functions
from Shared import *

#import libraries
import re

class DocumentScraper():
  """
  DocumentScapper provides the framework to take the textual content out of a web page and either save a minimised version of the web page or print out each of the paragraphs
  """

  def __init__(self,tags=['p','title'],ignoreWidth=100):
    self.setTags(tags)
    self.ignoreWidth = ignoreWidth

  def setTags(self,tags):
    """
    setTags sets the tags where content of interest is contained
    """

    self.regexTag = tags[0]

    for tag in tags[1:]:
      self.regexTag += r"|{}".format(tag)

  def setPage(self,url):
    """
    setPage is used to change the web page which is being scrapped when this method is called the title and paragraphs are set
    """

    self.webPage = getURL(url)
    self.url = url

    self.setTitle()
    self.setParagraphs()
    self.cleanParagraphs()

  def setTitle(self):
    """
    setTitle sets the class variable title to that of the web page title or if no title exists to the url
    """

    pattern = re.compile(r'<({0})[^>]*>(.*)</({0})>'.format('title'))
    matches = re.search(pattern, self.webPage, flags=0)

    if matches:
      self.title = matches.group(2)
    else:
      self.title = self.url.replace('/','')

  def setParagraphs(self):
    """
    setParagraphs looks for all content contained within any of the tags defined by setTags and produces a list of content and its position within the page
    """

    #match any content contained between tags
    pattern = re.compile(r'<({0})[^>]*>((.|\n)*?)</({0})>'.format(self.regexTag))

    self.paragraphs = []

    #for all matches push to paragraphs class variable
    for match in pattern.finditer(self.webPage):
      tagContent = match.group(2)

      if tagContent:
        text = parseHTML(tagContent)
        self.paragraphs.append([text,(match.start(),match.end())])


  def cleanParagraphs(self):
    """
    cleanParagraphs removes content from the paragraphs that is not useful
    """

    pattern = re.compile(r"<.*?>|[\t\n\r\f\v]*")

    for paragraph in self.paragraphs:
      paragraph[0] = re.sub(pattern,"",paragraph[0])

    for paragraph in self.paragraphs:
      if (len(paragraph[0]) < 20):
        self.paragraphs.remove(paragraph)

  def printParagraphs(self):
    """
    printParagraphs prints the first 100 characters of all paragraphs along with the start and end position within the web page
    """

    print self.url
    print self.title

    for paragraph in self.paragraphs:
      print [paragraph[0][:100],paragraph[1]]

  def saveParagraphs(self):
    """
    saveParagraphs saves all the paragraphs to a text file with a new line between each paragraph
    """

    fileContent = "{}\n".format(self.url)

    for paragraph in self.paragraphs:
      fileContent += "{} {}\n".format(paragraph[0].encode('ascii','ignore'),paragraph[1])

    if (len(self.paragraphs) > 0):
      averageLocation = sum([sum(paragraph[1])/2 for paragraph in self.paragraphs])/len(self.paragraphs)
      fileContent += "Average Paragraph Location: {} \n".format(averageLocation)
    if (len(self.paragraphs) > 1):
      gapSizes = [self.paragraphs[i+1][1][0]-self.paragraphs[i][1][1] for i in range(len(self.paragraphs)-1)]
      averageGap = sum(gapSizes)/len(gapSizes)
      fileContent += "List of Gap Sizes: {} \n".format(gapSizes)
      fileContent += "Average Size of Gap: {} \n".format(averageGap)

    filePath = "SavedPages/{}.txt".format(self.title)
    saveFile(filePath,fileContent)


if (__name__ == "__main__"):
    documentScraper = DocumentScraper()

    documentScraper.setPage("https://www.google.co.uk/search?client=safari&rls=en&q=bag+of+words+example&ie=UTF-8&oe=UTF-8&gfe_rd=cr&ei=BNOxVPOvGc7H8gfq24LABg#rls=en&q=simple+text+documents")
    documentScraper.saveParagraphs()

    documentScraper.setPage("http://www.newyorker.com/humor/borowitz-report/republicans-expose-obamas-college-plan-plot-make-people-smarter?intcid=mod-most-popular")
    documentScraper.saveParagraphs()

    documentScraper.setPage("http://www.newyorker.com/news/news-desk/blame-for-charlie-hebdo-murders?intcid=mod-most-popular")
    documentScraper.saveParagraphs()

    documentScraper.setPage("http://www.newyorker.com/humor/daily-shouts/bananaz-book-instructions-miley-cyrus")
    documentScraper.saveParagraphs()

    documentScraper.setPage("http://www.newyorker.com/magazine/2014/11/03/grain?intcid=mod-most-popular")
    documentScraper.saveParagraphs()


