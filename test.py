# -*- coding: utf-8 -*-
"""
@author: Rachel Rajan
"""
import const
#Clone tweepy from Github
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

class TweetListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)
        

def main():
    auth = tweepy.OAuthHandler(const.CONSUMER_KEY, const.CONSUMER_SECRET)
    auth.set_access_token(const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    twitterStream = Stream(auth, TweetListener())
    users = api.lookup_users(screen_names = ['github', 'twitter'])
#    for user in users:
#        print("\nscreen name: ", user.screen_name)
#        print("followers count: ", user.followers_count)
#        print("statues/tweets count: ", user.statuses_count)
#        print("url: ", user.url)
#        print("friends count: ", user.friends_count)
#        print("favourites count: ", user.favourites_count)
#    return
    
    #Display first 20 followers ad friends of twitter account
    twitter_user = api.get_user("SomeName")

    print("User details:")
    print("\nuser name: ", twitter_user.name)
    print("screen name: ", twitter_user.screen_name)
    print("user ID: ", twitter_user.id)
    print("Location: ", twitter_user.location)
    print("User description: ", twitter_user.description)
    print("The number of followers: ", twitter_user.followers_count)
    print("The number of friends: ", twitter_user.friends_count)
#    print("The number of tweets: ", twitter_user.retweet_count)
    print("User URL: ", twitter_user.profile_banner_url)

    print("\nFirst 20 Followers:")
    for twitter_user_follower in twitter_user.followers():
        print(twitter_user_follower.name)
    print("\nFriends:")
    for twitter_user_friends in twitter_user.friends():
        print(twitter_user_friends.name)


#call main()
if __name__ == "__main__":
    main()
    
    