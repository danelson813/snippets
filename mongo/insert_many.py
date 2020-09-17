
from stuff import user, password, secret_sauce
from datetime import datetime
import pymongo
import os

user = user
password = password

client = pymongo.MongoClient(secret_sauce)     # hooks up to the cluster
db = client.test   #choose the db
blog_collection = db.blog  # form the collection
posts = [
    {'user': 'halilylm', 'title': 'Second', 'content': 'I love MongoDB'},
    {'user': 'halilylm', 'title': 'Third', 'content': 'Flexible', 'category': 'Programming'},
    {'user': 'halilylm', 'title': 'End', 'content': 'Fast', 'post_date': datetime.now()}
]
insert_post = blog_collection.insert_many(posts)

print(insert_post.inserted_ids)  # output: 5ed022850f3c2884ce97a46f  outputs the _id for the entry