
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
for post in blog_collection.find({'user': 'halilylm'}):
    print(post)
# print(document)  # output: {'_id': ObjectId('5ed0254d97e5367d20c22e63'), 
# 'user': 'halilylm', 'title': 
# 'Second', 'content': 'I love MongoDB'}
# print(document.get('content'))  # output: I love MongoDB