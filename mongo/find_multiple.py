
from stuff import user, password, secret_sauce
from datetime import datetime
import pymongo
import os

user = user
password = password

client = pymongo.MongoClient(secret_sauce)     # hooks up to the cluster
db = client.test   #choose the db
blog_collection = db.blog  # form the collection

# document = blog_collection.find_one({'title': 'Second'})
for post in blog_collection.find({'content': {'$regex': '^I love'}}, {'_id': 0, 'post_date': 0, 'user': 0}):
    print(post)

# output: {'title': 'First post', 'content': 'I love Python'}
# output: {'title': 'Second', 'content': 'I love MongoDB'}