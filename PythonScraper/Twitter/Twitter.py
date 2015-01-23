"""
TwitterURLs.py is a class that can be used to obtain the URLs of user tweets
"""

#import sys
#sys.path.insert(0,'/var/pythonscripts/SocialMediaLinksRecommend/PythonScraper')
#print sys.path

#import all secret keys for twitter access
from Secret import *

#import TwitterAPI
from TwitterAPI import TwitterAPI

#Global Printing Variable
VERBOSE = False

class Twitter():
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
    self.setUser()

  def setUser(self,userName="owner"):

    self.userName = userName
    self.tweets = []
    self.favourites = []

  def getFollowers(self):
    """
    setFollowers sets the class variable to a list of user IDs that are
    following the authorised user
    """

    followers = []

    if (self.userName == 'owner'):
      response = self.api.request('followers/list',{'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    else:    
      response = self.api.request('followers/list',{'screen_name':self.userName,'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    
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
      response = self.api.request('friends/list',{'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    else:    
      response = self.api.request('friends/list',{'screen_name':self.userName,'skip_status':'true','include_user_entities':'false','count':self.responseCount})
    
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
      response = self.api.request('statuses/user_timeline',{'count':self.responseCount})
    else:
      response = self.api.request('statuses/user_timeline',{'screen_name':self.userName,'count':self.responseCount})

    self.tweets = []

    for item in response:
      self.tweets.append(item)

  def setFavourites(self):
    """
    setTweets adds a dictionary key value pair to the class variable tweets where
    the key is a userName (or owner if authorised user) and the value are tweets
    """
    
    if (self.userName == 'owner'):
      response = self.api.request('favorites/list',{'count':self.responseCount})
    else:
      response = self.api.request('favorites/list',{'screen_name':self.userName,'count':self.responseCount})

    self.favourites = []

    for item in response:
      self.favourites.append(item)

  def getURLs(self,tweetOrFavourite="tweet"):
    """
    setURLS adds a key value pair to the urls class variable where the key is
    a userName and the value is a list of recent URLs they have tweeted
    """

    if (tweetOrFavourite == "tweet"):
      if (len(self.tweets) == 0): self.setTweets()
      items = self.tweets
    elif (tweetOrFavourite == "favourite"):
      if (len(self.favourites) == 0): self.setFavourites()
      items = self.favourites
    else:
      raise ValueError("tweetOrFavourite must either be 'tweet' or 'favourite' not {}".format(tweetOrFavourite))

    urls = []

    for tweet in items:
      try:
        
        tweetUrls = tweet['entities']['urls']
      except KeyError:
        print "Key Error for user {}".format(userName)
        tweetUrls = []

      for url in tweetUrls:
        urls.append(url['expanded_url'])

    return urls


if (__name__ == "__main__"):

  twitter = Twitter(4)
  
  print(twitter.getFollowers())
  print(twitter.getURLs())
  print(twitter.getURLs("favourite"))
