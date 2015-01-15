from facepy import GraphAPI
from Secret import GRAPH_TOKEN
from Shared import *

class FacebookScraper():
  """FacebookScraper obtains friend and link information from the FacebookGraph API"""

  def __init__(self, accessToken):
    self.graph = GraphAPI(accessToken);

    self.friends = {}
    self.links = {}

  def setFriends(self):
    "Set a list of friends that correspond to the authorised user"

    #Set authorised individual
    me = self.graph.get('/me?fields=id,name')
    self.friends["me"] = me["name"] 

    #Obtain list of friends
    friends = self.graph.get('/me/friends?fields=id,name')

    #For all friends add id and name to friends object
    for friend in friends["data"]:
      self.friends[friend["id"]] = friend["name"]

  def setLinks(self,friendID="me"):
    "Set a list of links for the given userID"

    self.links[friendID] = []

    #Obtain shared links for given friendID
    links = self.graph.get('/{}/links'.format(friendID))

    #For each link add to the friend object
    for link in links["data"]:
      if ("link" in link.keys()):
        self.links[friendID].append(link["link"])

  def getLinks(self,friendID="me"):
    """ getLinks returns the links for the given userID"""

    if (friendID not in self.links.keys()): self.setLinks(friendID)

    return self.links[friendID]

  def printData(self):
    """pintData prints all the class data with the links shortened for display"""

    for key,data in self.friends.items():
      print(key,data)

    for friendID,links in self.links.items():
      print(self.friends[friendID])
      for link in links:
        print("\t{}".format(link[:100]))

  def saveData(self,filename):
    """saveData saves all data associated with class in JSON file"""

    saveObject = []

    for friendID in self.friends.keys():
      saveObject.append({
        "id" : friendID,
        "name" : self.friends[friendID],
        "links" : self.getLinks(friendID)
        })

    saveJSON(filename,saveObject)

if (__name__ == "__main__"):
  #get_extended_access_token(ACCESS_TOKEN,APP_ID,APP_SECRET)
  facebookScraper = FacebookScraper(GRAPH_TOKEN)
  facebookScraper.setFriends()
  facebookScraper.saveData("friendLinks.JSON")