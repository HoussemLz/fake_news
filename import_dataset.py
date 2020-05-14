import pymongo

import os
from fnmatch import fnmatch
from pymongo import MongoClient
import json
import datetime

# root = r'C:\Useers\salah\Desktop\master project\pheme rhumour data set\pheme-rnr-dataset\charliehebdo'
root = r'D:\Housem suit data\Filtered_data_set2015_p1\Docs\29_07_2015_3'
dbName = "Data_set2015"

client = MongoClient('localhost', 27017)
db = client[dbName]
tweets = db.tweets
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*"):
            filePath = os.path.join(path, name)
            file1 = open(filePath, 'r', encoding="utf-8")
            Lines = file1.readlines()
            for line in Lines:
                json_tweet = json.loads(line.strip())
                if "delete" in json_tweet:
                    continue
                print(line.strip())
                tweet_id = tweets.insert_one(json_tweet).inserted_id
                print(tweet_id)
            file1.close()


