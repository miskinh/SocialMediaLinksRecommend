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

  def __init__(self,responseCount=200):

    #set response count
    self.responseCount = responseCount

    #configure TwitterAPI AUTH
    self.api = TwitterAPI(CONSUMER_KEY,
                          CONSUMER_SECRET, 
                          ACCESS_TOKEN_KEY, 
                          ACCESS_TOKEN_SECRET)

    #set class variables to store responses
    self.tweets = {}
    self.urls = {}
    self.followers = {}
    self.friends = {}

  def setFollowers(self,screenName='owner'):
    """
    setFollowers sets the class variable to a list of user IDs that are
    following the authorised user
    """

    self.followers[screenName] = []

    if (screenName == 'owner'):
      response = self.api.request('followers/list',{'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    else:    
      response = self.api.request('followers/list',{'screen_name':screenName,'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    
    for item in response:
      if ('users' not in item.keys()):
        print(item)
        continue
      for user in item['users']:
        # for key, value in user.items():
        #   print(key,value)
        self.followers[screenName].append(user['screen_name'])

  def setFriends(self,screenName='owner'):
    """
    setFriends sets the class variable to a list of user IDs that are
    following the authorised user
    """

    self.friends[screenName] = []

    if (screenName == 'owner'):
      response = self.api.request('friends/list',{'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    else:    
      response = self.api.request('friends/list',{'screen_name':screenName,'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    
    for item in response:
      if ('users' not in item.keys()):
        print(item)
        continue
      for user in item['users']:
        # for key, value in user.items():
        #   print(key,value)
        self.friends[screenName].append(user['screen_name'])

  
  def setTweets(self,screenName='owner'):
    """
    setTweets adds a dictionary key value pair to the class variable tweets where
    the key is a screenName (or owner if authorised user) and the value are tweets
    """
    
    if (screenName == 'owner'):
      response = self.api.request('statuses/user_timeline',{'count':self.responseCount})
    else:
      response = self.api.request('statuses/user_timeline',{'screen_name':screenName,'count':self.responseCount})

    self.tweets[screenName] = []

    for item in response:
      self.tweets[screenName].append(item)

  def setURLs(self,screenName='owner'):
    """
    setURLS adds a key value pair to the urls class variable where the key is
    a screenName and the value is a list of recent URLs they have tweeted
    """

    if (screenName not in self.tweets.keys()): self.setTweets(screenName)

    self.urls[screenName] = []

    for tweet in self.tweets[screenName]:
      try:
        urls = tweet['entities']['urls']
      except KeyError:
        print "Key Error for user {}".format(screenName)
        urls = []

      for url in urls:
        self.urls[screenName].append(url['expanded_url'])

  def getFollowers(self,screenName='owner'):
    "printFollowers prints all followers in the class variable followers"

    if (screenName not in self.followers.keys()): self.setFollowers(screenName)

    if VERBOSE:
      for follower in self.followers[screenName]:
        print follower

    return self.followers[screenName]

  def getFriends(self,screenName='owner'):
    "printFriends prints all followers in the class variable followers"

    if (screenName not in self.friends.keys()): self.setFriends(screenName)

    if VERBOSE:
      for friend in self.friends[screenName]:
        print friend

    return self.friends[screenName]

  def getTweets(self,screenName='owner'):
    "printTweets prints all the tweet text for the given screenName"

    if (screenName not in self.tweets.keys()): self.setTweets(screenName)

    tweets = []

    for tweet in self.tweets[screenName]:
      if VERBOSE: print tweet['text']
      tweets.append(tweet['text'])

    return tweets

  def getURLs(self,screenName='owner'):
    "printURLs prints all the URLs shared by the given screenName"

    if (screenName not in self.urls.keys()): self.setURLs(screenName)

    if VERBOSE:
      for url in self.urls[screenName]:
        print url

    return self.urls[screenName]

  def getAllURLs(self):
    "getAllURLs gets all the the URLs shared by a users followers"

    self.getFollowers()
    self.getFriends()

    #set the urls for owner
    self.setURLs()

    #get the urls for all owners
    for friend in self.friends:
      self.setURLs(friend)

    for follower in self.followers:
      self.setURLs(follower)

    #return the urls dictionary object
    return self.urls

if (__name__ == "__main__"):
  VERBOSE = True
  twitterURLs = TwitterURLs()
  
  #Get list of twitter followers
  twitterURLs.getFollowers()
  # print("============")
  twitterURLs.getFriends()

  # #Get tweets and URLs for AUTH user
  # twitterURLs.getTweets()
  # twitterURLs.getURLs()

  # #Get tweets and URLs for user with screenName 2815238795
  # twitterURLs.getTweets('JamesDolman')
  # twitterURLs.getURLs('JamesDolman')
