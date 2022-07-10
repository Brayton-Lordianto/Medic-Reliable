# this file takes care of login and signup

# do pip install pymongo dnspython
import pymongo

# set up database
url = "mongodb+srv://Cherlord1:Cherlord1@cluster0.2img3.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client["Database"]

account_collection = db["Accounts"]
username_field = 'username'
password_field = 'password'

# test db is working -- also go to testdb.py
print(f'the database contained is {db.list_collection_names()}')
def get_db(): return account_collection

# signup using username and passwrod -> (Success, Id)
def signup(username, password):
    # if already exists return false, none
    found = account_collection.find_one({ username_field : username })
    if found: return False, None
    
    # else just insert the new document
    doc = {
        username_field : username,
        password_field : password
    }
    
    account_collection.insert_one(doc)
    return True, account_collection.find_one({ username_field : username })


# login using username and password -> (Success, Id)
def login(username, password):
    record = account_collection.find_one({ username_field : username })
    
    # if not exists or wrong password, send false, none
    if not record or record[password_field] != password:
        return False, None
    return True, record