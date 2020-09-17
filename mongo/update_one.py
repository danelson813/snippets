
from stuff import user, password, secret_sauce
from datetime import datetime
import pymongo
import os

user = user
password = password

client = pymongo.MongoClient(secret_sauce)     # hooks up to the cluster
db = client.test   #choose the db
blog_collection = db.blog  # form the collection

query = {'content': 'I love MongoDB'}
print(blog_collection.find_one(query))
# output: {'_id': ObjectId('5ed12a90a2ea2942ec2a23d7'),
# 'user': 'halilylm', 'title': 'Second', 'content': 'I love MongoDB'}

new_document = {'$set': {'content': 'I love MongoDB and Python', 'title': 'Updated Post'}}
update_post = blog_collection.update_one(query, new_document, upsert=False)
print(update_post.matched_count)  # output: 1

updated_document = blog_collection.find_one({'title': 'Updated Post'})
print(updated_document)
# output: {'_id': ObjectId('5ed12a90a2ea2942ec2a23d7'), 'user': 'halilylm',
# 'title': 'Updated Post', 'content': 'I love MongoDB and Python'}