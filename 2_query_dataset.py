#Update isReply ::: db.getCollection('tweets').update({"in_reply_to_status_id": "null" }, { $set: {"isReply": "N" } }, false, true)

#Fetch db with ocndition : db.getCollection('tweets').find({"truncated": "false"})

#delete field from all docuement : db.getCollection('tweets').update({}, {$unset: {contributors:1}}, false, true);

# Fields is not null : db.getCollection('tweets').find({"coordinates": { $ne: "null" }})

# check field existe
# db.getCollection('tweets').find( { 'evaluation': {'$exists': true } })

#delete all document if field don't exist :
# db.getCollection('tweets').remove({"evaluation": {"$exists": false }})

#_____________________________________________________________________
#Export to csv from mongodb :
#mongoexport --db Data_set2015 --collection tweets --type=csv --fields topic_id,evaluation --out C:\Users\houssem\Desktop\Pheme\results.csv


#Add_ field to all document : db.getCollection('tweets').update({}, { $set: {"evaluation": 1 } }, false, true);
#Add_ field to all document : db.getCollection('tweets').update({}, { $set: {"topic": "charlie" } }, false, true);


#Add_ fiels if evaluation_ not exist _________RUMOUR_____________________:
#db.getCollection('tweets').update({'evaluation': {$exists : false}}, {$set: {'evaluation': 1 }}, false, true)

#Add_ fiels if evaluation_ not exist _________NON_rumour_____________________:
#db.getCollection('tweets').update({'evaluation': {$exists : false}}, {$set: {'evaluation': 0 }}, false, true)



#Add_ fiels if topic not exist :
##db.getCollection('tweets').update({'topic': {$exists : false}}, {$set: {'topic': 'sydneysiege' }}, false, true)

#db.getCollection('tweets').update({}, {$unset: {in_reply_to_status_id_str:1}}, false, true);
#db.getCollection('tweets').find({"place": { $ne: "null" }})