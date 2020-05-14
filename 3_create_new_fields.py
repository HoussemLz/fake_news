import pymongo

import os
from fnmatch import fnmatch
from pymongo import MongoClient
import json
import datetime

dbName = "pheme_copy"
client = MongoClient('localhost', 27017)
db = client[dbName]
tweets = db.tweets

for tweet in tweets: #parcourir mongo tweets dataset
    id = str(tweet['id'])) #for each id_ or each tweet
    hashtag_count = db.tweets.find({'hashtags' : { $gte: 0 }}).count() #read its hashtags fileds and count number of element (hastags)
    print(hashtag_count)
    #create news fields named : nb_of_hastags and insert the value calculated
    tweet["hashtag_count"] = hashtag_count
    db.tweets.update_one({"id": int(id)}, {"$set": {"hashtag_count": hashtag_count}})

