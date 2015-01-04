"""
TwitterURLs.py is a class that can be used to obtain the URLs of user tweets
"""

#import all secret keys for twitter access
from Secret import *

#import TwitterAPI
from TwitterAPI import TwitterAPI

class TwitterURLs():
  """
  Twitter URLs enables access to the URLs posted by the authorised user and
  the followers of that user
  """

  def __init__(self):

    #configure TwitterAPI AUTH
    self.api = TwitterAPI(CONSUMER_KEY,
                          CONSUMER_SECRET, 
                          ACCESS_TOKEN_KEY, 
                          ACCESS_TOKEN_SECRET)

    #set class variables to store responses
    self.tweets = {}
    self.urls = {}
    self.followers = []

  def setFollowers(self):
    """
    setFollowers sets the class variable to a list of user IDs that are
    following the authorised user
    """

    response = self.api.request('followers/ids')
    
    for item in response:
      self.followers = item['ids']
  
  def setTweets(self,userID='owner'):
    """
    setTweets adds a dictionary key value pair to the class variable tweets where
    the key is a userID (or owner if authorised user) and the value are tweets
    """
    
    if (userID == 'owner'):
      response = self.api.request('statuses/user_timeline')
    else:
      response = self.api.request('statuses/user_timeline',{'user_id':userID})

    self.tweets[userID] = []

    for item in response:
      self.tweets[userID].append(item)

  def setURLs(self,userID='owner'):
    """
    setURLS adds a key value pair to the urls class variable where the key is
    a userID and the value is a list of recent URLs they have tweeted
    """

    self.urls[userID] = []

    for tweet in self.tweets[userID]:
      urls = tweet['entities']['urls']

      for url in urls:
        self.urls[userID].append(url['expanded_url'])

  def printFollowers(self):
    "printFollowers prints all followers in the class variable followers"

    for follower in self.followers:
      print follower

  def printTweets(self,userID='owner'):
    "printTweets prints all the tweet text for the given userID"

    for tweet in self.tweets[userID]:
      print tweet['text']

  def printURLs(self,userID='owner'):
    "printURLs prints all the URLs shared by the given userID"

    for url in self.urls[userID]:
      print url

if (__name__ == "__main__"):
  twitterURLs = TwitterURLs()

  #Set list of followers and print
  twitterURLs.setFollowers()
  twitterURLs.printFollowers()

  #Get tweets and URLs for AUTH user and print
  twitterURLs.setTweets()
  twitterURLs.setURLs()
  twitterURLs.printTweets()
  twitterURLs.printURLs()

  #Get tweets and URLs for user with userID 2815238795
  twitterURLs.setTweets('2815238795')
  twitterURLs.setURLs('2815238795')
  twitterURLs.printTweets('2815238795')
  twitterURLs.printURLs('2815238795')