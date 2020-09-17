
from stuff import user, password, secret_sauce
from datetime import datetime
import pymongo
import os

user = user
password = password

client = pymongo.MongoClient(secret_sauce)     # hooks up to the cluster
db = client.test   #choose the db
blog_collection = db.blog  # form the collection

del_document = blog_collection.delete_one({'title': 'First post'})
print(del_document.deleted_count)  # output: 1