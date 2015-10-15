#import tweepy

"""requires python-twitter"""
import twitter
import csv
import time
from os import environ

CONSUMER_KEY        = environ.get("CONSUMER_KEY")
CONSUMER_SECRET     = environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY    = environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = environ.get("ACCESS_TOKEN_SECRET")

USER_FEATURE_TABLE = (
                       ("user_id",          lambda x: x.id),
                       ("created_at",       lambda x: x.created_at),
                       ("favourites_count", lambda x: x.favourites_count),
                       ("followers_count",  lambda x: x.followers_count),
                       ("following_count",  lambda x: x.friends_count),
                       ("geo_enabled",      lambda x: x.geo_enabled),
                       ("lang",             lambda x: x.lang),
                       ("location",         lambda x: x.location),
                       ("time_zone",        lambda x: x.time_zone),
                       ("statuses_count",   lambda x: x.statuses_count)
                       )

TWEET_FEATURE_TABLE = (
                       ("tweet_id",                lambda x: x.id),
                       ("user_id",                 lambda x: x.user.id),
                       ("created_at",              lambda x: x.created_at),
                       ("text",                    lambda x: unicoder(x.text)),
                       ("longitude",               lambda x: x.coordinates['coordinates'][0] if x.coordinates is not None else None),
                       ("latitude",                lambda x: x.coordinates['coordinates'][1] if x.coordinates is not None else None),
                       ("place",                   lambda x: x.place["full_name"] if x.place is not None else None),
                       ("favorited",               lambda x: x.favorited),
                       ("favorite count",          lambda x: x.favorite_count),
                       ("in_reply_to_user_id",     lambda x: x.in_reply_to_user_id),
                       ("in_reply_to_status_id",   lambda x: x.in_reply_to_status_id),
                       ("retweet_count",           lambda x: x.retweet_count),
                       ("source",                  lambda x: x.source),
                       ("lang",                    lambda x: x.lang),
                       ("url_count",               lambda x: len(x.urls)),
                       ("mention_count",           lambda x: len(x.user_mentions)),
                       ("hashtags",                lambda x: x.hashtags),
                       )

def unicoder(string):
  """helper function that is necessary for correct unicode encoding"""
  #return unicode(string).encode("utf-8")
  return string.decode('utf-8')
def api_setup(consumer_key,consumer_secret,access_key,access_secret):
  """function to set up api"""
  #auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
  #auth.set_access_token(access_key,access_secret)
  #return tweepy.API(auth)
  api = twitter.Api(consumer_key        = consumer_key,
                    consumer_secret     = consumer_secret,
                    access_token_key    = access_key,
                    access_token_secret = access_secret)

  return api

def read_userids(filename):
  """opens id file. Make sure that first line of id file is empty
  filename paramter is a string with the file's extension"""
  id_file=open(filename,"r")
  ids=id_file.readlines()[1:]
  ids=[(unicode(i).encode("utf-8")).replace("\n","") for i in ids]
  return ids

def extract_tweets_from_user_timeline(api, filename, output_file):
  with open(output_file, "w") as output:
    csv_writer = csv.writer(output)
    csv_writer.writerow([f[0] for f in TWEET_FEATURE_TABLE])
    with open(filename, 'r') as csvf:
      csv_reader = csv.DictReader(csvf)
      for row in csv_reader:
        user_id = row["id"]
        print "Getting timeline of {}".format(user_id)
        try:
          if not api.GetUser(user_id=user_id).protected:
            try:
              for s in api.GetUserTimeline(user_id=user_id):
                features = [f[1](s) for f in TWEET_FEATURE_TABLE]
                csv_writer.writerow(features)
            except twitter.error.TwitterError:
              print "entering sleep"
              time.sleep(960)
              print "exiting sleep"
              continue
            except UnicodeEncodeError as e:
              print e.message
              #print unicoder(features[3])
              #print features
        except twitter.error.TwitterError:
          print "entering sleep"
          time.sleep(960)
          print "exiting sleep"
          continue


if __name__ == "__main__":
  api = api_setup(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  extract_tweets_from_user_timeline(api, "data/twitter_identity.csv", "data/test1")