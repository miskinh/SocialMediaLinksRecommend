"""
TwitterNetwork
This functionality finds all possible friend connections and obtains shared links
"""

from TwitterURLs import TwitterURLs

def findFriends():
  "findFriends finds all the friends of friends for the authorised user"

  # Construct TwitterURLs with a return limit of 3
  twitterURLs = TwitterURLs(3)
  friends = twitterURLs.getFriends()

  # For all friends
  for friend in friends:
    print(friend)

    #  Find friends friends
    friendFriends = twitterURLs.getFriends(friend)
    for friendFriend in friendFriends:
      print("\t" + friendFriend)

      # Find friends friends friends
      friendFriendFriends = twitterURLs.getFriends(friendFriend)
      for friendFriendFriend in friendFriendFriends:
        print("\t\t" + friendFriendFriend)

def buildNetwork(degrees):
  "finds all the people in a persons network to a number of degrees"
  twitterURLs = TwitterURLs(1)

  network = {}
  network[0] = twitterURLs.getFriends()

  for i in range(1,degrees):
    network[i] = []
    for node in network[i-1]:
      network[i] += twitterURLs.getFriends(node)

  print(network)

  urls = {}

  for i in range(0,degrees):
    urls[i] = []
    for node in network[i]:
      urls[i]+=twitterURLs.getTweets(node)

  print(urls)


def getLinks():
  "getLinks returns the links for a number of specified users"

  twitterURLs = TwitterURLs(3)

  # Obtain links for a 1st connection
  urls = twitterURLs.getURLs("ignaciowillats")
  print(urls)

  # Obtain links for a 2st connection
  urls = twitterURLs.getURLs("edtech_rr")
  print(urls)

  # Obtain links for a 3rd connection - NOT WORKING
  urls = twitterURLs.getURLs("DavidatBAM")
  print(urls)

if (__name__ == "__main__"):

  buildNetwork(3)
  #getLinks()