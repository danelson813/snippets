
from stuff import user, password, secret_sauce
from datetime import datetime
import pymongo
import os

user = user
password = password

client = pymongo.MongoClient(secret_sauce)     # hooks up to the cluster
db = client.test   #choose the db
blog_collection = db.blog  # form the collection


query = {'user': 'halilylm'}
new_user = {'$set': {'user': 'halil'}}
update = blog_collection.update_many(query, new_user)
print(update.matched_count)  # 3