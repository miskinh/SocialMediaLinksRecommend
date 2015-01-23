"""
TwitterNetwork
This functionality finds all possible friend connections and obtains shared links
"""

from Twitter import Twitter

class TwitterNetwork(Twitter):
  """docstring for TwitterNetwork"""

  def __init__(self, responseCount=200):
    super(TwitterNetwork, self).__init__(responseCount)

  def getUser(self,userName="owner"):
    "findFollowers finds all the followers of followers for the authorised user"

    user = {}

    self.setUser(userName)
    user["userName"] = userName
    user["friends"] = self.getFriends()
    user["followers"] = self.getFollowers()
    user["postURLs"] = self.getURLs("tweets")
    user["likeURLs"] = self.getURLs("favourites")

    return user
