import tweepy
import csv
import random

consumer_key = "gk0TbKe5XNULjdtbFMC9N9eOC"
consumer_secret = "HLdvWj9HZ833HU1uzEBC0HAWZhE2u9vaEem3oz9vCYNcw1UvvD"
access_token = "952357334843617282-SI1Iy1sS2rqmiJvbuGPy6y1GY5KV3MN"
access_token_secret = "jcnaNGXyeSl3YCw9Z9buOlswJYz85FiO6kJvetET0cEiV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

FileHeader = ['DayOfWeek','Time']
CSVfile = open("record.csv", "a")
writer = csv.writer(CSVfile)
writer.writerow(FileHeader)
CSVfile.close()

twid = random.choice(range(90,999999999))
n = 0
while n < 3000:
    CSVfile = open("record.csv", "a")
    try:
        tweet = api.get_status(twid)
        if tweet.text.lower().find("good morning") >= 0:
            h = int(tweet.created_at.strftime("%H"))
            ms = int(tweet.created_at.strftime("%M"))/60
            writer.writerow([tweet.created_at.weekday(),h+ms])
            n += 1
            twid = random.choice(range(90,999999999))
        else:
            twid = random.choice(range(90,999999999))
    except:
        twid = random.choice(range(90,999999999))
    finally:        
        CSVfile.close()