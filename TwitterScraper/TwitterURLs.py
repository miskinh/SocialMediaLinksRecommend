"""
TwitterURLs.py is a class that can be used to obtain the URLs of user tweets
"""

#import all secret keys for twitter access
from Secret import *

#import TwitterAPI
from TwitterAPI import TwitterAPI

#Global Printing Variable
VERBOSE = False

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

    self.followers = []

    response = self.api.request('followers/list',{'skip_status':'true','include_user_entities':'false'})
    
    for item in response:
      for user in item['users']:
        self.followers.append(user['id'])
        #self.followers.append(user['screen_name'])

  
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

    if (userID not in self.tweets.keys()): self.setTweets(userID)

    self.urls[userID] = []

    for tweet in self.tweets[userID]:
      urls = tweet['entities']['urls']

      for url in urls:
        self.urls[userID].append(url['expanded_url'])

  def getFollowers(self):
    "printFollowers prints all followers in the class variable followers"

    if (len(self.followers) == 0): self.setFollowers()

    if VERBOSE:
      for follower in self.followers:
        print follower

    return self.followers

  def getTweets(self,userID='owner'):
    "printTweets prints all the tweet text for the given userID"

    if (userID not in self.tweets.keys()): self.setTweets(userID)

    tweets = []

    for tweet in self.tweets[userID]:
      if VERBOSE: print tweet['text']
      tweets.append(tweet['text'])

    return tweets

  def getURLs(self,userID='owner'):
    "printURLs prints all the URLs shared by the given userID"

    if (userID not in self.urls.keys()): self.setURLs(userID)

    if VERBOSE:
      for url in self.urls[userID]:
        print url

    return self.urls[userID]

  def getAllURLs(self):
    "getAllURLs gets all the the URLs shared by a users followers"

    if (len(self.followers) == 0): self.setFollowers()

    #set the urls for owner
    self.setURLs()

    #get the urls for all owners
    for follower in self.followers:
      setURLs(follower)

    #return the urls dictionary object
    return self.urls


def run():
  VERBOSE = True
  twitterURLs = TwitterURLs()
  
  #Get list of twitter followers
  twitterURLs.getFollowers()

  return

  #Get tweets and URLs for AUTH user
  twitterURLs.getTweets()
  twitterURLs.getURLs()

  #Get tweets and URLs for user with userID 2815238795
  twitterURLs.getTweets('2815238795')
  twitterURLs.getURLs('2815238795')

if (__name__ == "__main__"):
  run()
