"""
TwitterURLs.py is a class that can be used to obtain the URLs of user tweets
"""

#import all secret keys for twitter access
from Secret import *

#import external modules
import time
from datetime import  datetime, timedelta
from TwitterAPI import TwitterAPI

#Global Printing Variable
VERBOSE = False

class Twitter(object):
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
    self.requests = {}
    self.setUser()

  def setUser(self,userName="owner"):

    self.userName = userName
    self.tweets = []
    self.favourites = []

  def request(self,url,parameters={}):

    return self.api.request(url,parameters)

    # Find the current time
    now = datetime.now()

    # Find the time of the last call or make one up
    if (url in self.requests.keys()):
      lastCall = self.requests[url]
    else:
      lastCall = datetime.now() - timedelta(minutes=1)

    # Compute the time since last call
    sinceLastCall = timedelta(datetime.now(),lastCall)

    # If required sleep for a period of time
    if (sinceLastCall < timedelta(minutes=1)):
      time.sleep(sinceLastCall - timedelta(minutes=1))

    # Call request and update last call time
    self.requests[url] = datetime
    return self.api.request(url,parameters)

  def getFollowers(self):
    """
    setFollowers sets the class variable to a list of user IDs that are
    following the authorised user
    """

    followers = []

    if (self.userName == 'owner'):
      response = self.request('followers/list',{'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    else:    
      response = self.request('followers/list',{'screen_name':self.userName,'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    
    for item in response:
      if ('users' not in item.keys()):
        print(item)
        continue
      for user in item['users']:
        followers.append(user['screen_name'])

    return followers

  def getFriends(self):
    """
    setFriends sets the class variable to a list of user IDs that are
    following the authorised user
    """

    friends = []

    if (self.userName == 'owner'):
      response = self.request('friends/list',{'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    else:    
      response = self.request('friends/list',{'screen_name':self.userName,'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    
    for item in response:
      if ('users' not in item.keys()):
        print(item)
        continue
      for user in item['users']:
        friends.append(user['screen_name'])

    return friends
  
  def setTweets(self):
    """
    setTweets adds a dictionary key value pair to the class variable tweets where
    the key is a userName (or owner if authorised user) and the value are tweets
    """
    
    if (self.userName == 'owner'):
      response = self.request('statuses/user_timeline',{'count':self.responseCount})
    else:
      response = self.request('statuses/user_timeline',{'screen_name':self.userName,'count':self.responseCount})

    self.tweets = []

    for item in response:
      self.tweets.append(item)

  def setFavourites(self):
    """
    setTweets adds a dictionary key value pair to the class variable tweets where
    the key is a userName (or owner if authorised user) and the value are tweets
    """
    
    if (self.userName == 'owner'):
      response = self.request('favorites/list',{'count':self.responseCount})
    else:
      response = self.request('favorites/list',{'screen_name':self.userName,'count':self.responseCount})

    self.favourites = []

    for item in response:
      self.favourites.append(item)

  def getURLs(self,tweetOrFavourite="tweets"):
    """
    setURLS adds a key value pair to the urls class variable where the key is
    a userName and the value is a list of recent URLs they have tweeted
    """

    if (tweetOrFavourite == "tweets"):
      if (len(self.tweets) == 0): self.setTweets()
      items = self.tweets
    elif (tweetOrFavourite == "favourites"):
      if (len(self.favourites) == 0): self.setFavourites()
      items = self.favourites
    else:
      raise ValueError("tweetOrFavourite must either be 'tweets' or 'favourites' not {}".format(tweetOrFavourite))

    urls = []

    for tweet in items:
      try:
        
        tweetUrls = tweet['entities']['urls']
      except KeyError:
        print "Key Error for user {}".format(self.userName)
        tweetUrls = []

      for url in tweetUrls:
        urls.append(url['expanded_url'])

    return urls


if (__name__ == "__main__"):

  twitter = Twitter(4)
  
  print(twitter.getFollowers())
  print(twitter.getURLs())
  print(twitter.getURLs("favourite"))
