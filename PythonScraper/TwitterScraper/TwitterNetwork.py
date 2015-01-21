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

def getLinks():
  "getLinks returns the links for a number of specified users"

  twitterURLs = TwitterURLs(10)

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
  getLinks()