
from stuff import user, password, secret_sauce
from datetime import datetime
import pymongo
import os

user = user
password = password

client = pymongo.MongoClient(secret_sauce)     # hooks up to the cluster
db = client.test   #choose the db
blog_collection = db.blog  # form the collection

del_posts = blog_collection.delete_many({'user': 'halilylm'})
print(del_posts.deleted_count)  # output: 3