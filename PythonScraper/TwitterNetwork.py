"""
TwitterNetwork
This functionality finds all possible friend connections and obtains shared links
"""

from Twitter.Twitter import Twitter
from DataAccess.Create import Create

class TwitterNetwork(Twitter):
  """docstring for TwitterNetwork"""
  def __init__(self, arg):
    super(TwitterNetwork, self).__init__()
    self.arg = arg
    

class TwitterNetwork(object):
  """docstring for TwitterNetwork"""

  def __init__(self):
    self.twitterURLs = TwitterURLs(200)
    

  def getUser(userName="owner"):
    "findFollowers finds all the followers of followers for the authorised user"

    user = {}

    user["friends"] = self.twitterURLs.getFriends(userName)
    user["followers"] = self.twitterURLs.getFollowers(userName)
    user["urls"] = self.twitterURLs.getURLs(userName)

    return user



if (__name__ == "__main__"):

  create = Create()
  userName = "hpgmiskin"
  user = getUser()
  create.addUser(
    userName,
    followerUserNames=user["followers"],
    friendUserNames=user["friends"],
    urls=user["urls"]
    )
  
  for follower in followers:
    followers,urls = findFollowers(follower)
    create.addUser(follower,followers[:5],urls)

