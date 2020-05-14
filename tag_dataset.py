import os
from fnmatch import fnmatch
from pymongo import MongoClient
import json
import datetime
import csv
#read qrels file
dbName = "Data_set2015"
evaluated_tweets_file_path = r"C:\Users\houssem\Desktop\test_data\Evaluation\\qrels.txt"
#open mongo db connect
client = MongoClient('localhost', 27017)
db = client[dbName]
tweets = db.tweets
#open the file qrels
with open(evaluated_tweets_file_path) as f:
    lis = [line.split() for line in f]  # create a list of lists
    # for each line of qrels, copy id + eval
    for i, x in enumerate(lis):  # print the list items
        topic_id = x[0]
        id = x[2]
        evaluation = x[3]
        print(id)
        #find the tweet in db with the same id_
        tweet = tweets.find_one({"id": int(id)})
        if tweet is None :
            continue
        #if "_id" not in tweet:
        #   continue
        else:

            if evaluation in tweet :
                continue
            else:

                tweet["evaluation"] = evaluation
                tweet["topic_id"] = topic_id
                print(tweet)
                #update the tweet in db
                db.tweets.update_one({"id": int(id)}, {"$set": {"evaluation": evaluation,"topic_id": topic_id}})


        # add column evalution to tweet json
        # check field existe
        # db.getCollection('tweets').find( { 'evaluation': { '$exists': true } } )
