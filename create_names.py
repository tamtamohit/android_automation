import json
from pymongo import MongoClient


collection = MongoClient()['gmail_accounts'].data



fo = open('data.json','r')
data = json.loads(fo.read())
    # print i
# filo_magic = json.loads(fo.read())
for i in data:
    if len(i['first_name']) == 0 or len(i['last_name']) == 0:
        continue

    name = i['first_name'].replace(' ','') + i['last_name'].replace(' ','')

    i['combine_name'] = name.lower()

    collection.insert(i)