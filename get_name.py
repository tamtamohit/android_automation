'''
All emails has been saved to mongodb.
DB name: gmail_accounts
Collection name: data

'''

from random import choice,randint
from pymongo import MongoClient
collection = MongoClient()['gmail_accounts'].data


alphabets = 'qwertyuiopasdfghjklzxcvbnm'
alphabets_other = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def fields():
    name_dict = collection.find_one({"email":{'$exists':0}})
    print name_dict
    # return 'ravi', 'ram', 'raviram67259', 'sanIjk99q'
    first_name = name_dict['first_name']
    # for i in xrange(randint(5,8)):
    #     first_name  += choice(alphabets)

    last_name = name_dict['last_name']


    # email = ''
    email = name_dict['combine_name']
    for i in xrange(randint(7,9)):
        email += str(randint(0,9))

    password = ''
    for i in xrange(randint(8,11)):
        password += choice(alphabets_other)

    mongo_id =  name_dict['_id']

    return first_name, last_name, email, password, mongo_id
# first_name =

if __name__ == '__main__':
    print fields()