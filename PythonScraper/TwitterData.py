"""
TwitterNetwork
This functionality finds all possible friend connections and obtains shared links
"""

from Twitter.TwitterNetwork import TwitterNetwork
from Data.Create import Create

create = Create()
twitter = TwitterNetwork(10)

def getOwnerNetwork():

  user = twitter.getUser()
  user["userName"] = "hpgmiskin"
  create.addUserObject(user)

  for follower in user["followers"]:
    getUserNetwork(follower)

  for friend in user["friends"]:
    getUserNetwork(friend)

def getUserNetwork(userName):

  user = twitter.getUser(userName)
  user["userName"] = userName
  create.addUserObject(user)

  for follower in user["followers"]:
    user = twitter.getUser(follower)
    create.addUserObject(user)

  for friend in user["friends"]:
    user = twitter.getUser(follower)
    create.addUserObject(user)

if __name__ == "__main__":
  getOwnerNetwork()