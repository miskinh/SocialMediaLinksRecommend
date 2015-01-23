"""
TwitterNetwork
This functionality finds all possible friend connections and obtains shared links
"""

from TwitterScraper.TwitterURLs import TwitterURLs
from DataAccess.Create import Create

def getUser(userName="owner"):
  "findFollowers finds all the followers of followers for the authorised user"

  user = {}

  # Construct TwitterURLs with a return limit of 3
  twitterURLs = TwitterURLs(200)
  user["friends"] = twitterURLs.getFriends(userName)
  user["followers"] = twitterURLs.getFollowers(userName)
  user["urls"] = twitterURLs.getURLs(userName)

  return user

def findFollowers(userName="owner"):
  "findFollowers finds all the followers of followers for the authorised user"

  # Construct TwitterURLs with a return limit of 3
  twitterURLs = TwitterURLs(100)
  followers = twitterURLs.getFollowers(userName)
  urls = twitterURLs.getURLs(userName)

  return followers,urls

def printFollowers():
  "findFollowers finds all the followers of followers for the authorised user"

  # Construct TwitterURLs with a return limit of 3
  twitterURLs = TwitterURLs(3)
  followers = twitterURLs.getFollowers()

  # For all followers
  for follower in followers:
    print(follower)

    #  Find followers followers
    followerFollowers = twitterURLs.getFollowers(follower)
    for followerFollower in followerFollowers:
      print("\t" + followerFollower)

      # Find followers followers followers
      followerFollowerFollowers = twitterURLs.getFollowers(followerFollower)
      for followerFollowerFollower in followerFollowerFollowers:
        print("\t\t" + followerFollowerFollower)

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
  create = Create()
  userName = "hpgmiskin"
  followers,urls = findFollowers()
  create.addUser(userName,followers,urls)
  
  for follower in followers:
    followers,urls = findFollowers(follower)
    create.addUser(follower,followers[:5],urls)
