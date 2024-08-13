from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
            
    # Create CRUD function
    # data = dictionary of key/value pairs
    # Returns a boolean depending on the success of the function
    def create(self, data):
        try:
            result = self.database.animals.insert_one(data)
            return result.acknowledged
        except Exception as e:
            #print("An error occured during the write ::", e)
            return False

    # Read CRUD function
    # data = dictionary of key/value pair(s)
    # Returns list of objects
    def read(self, data):
        try:
            return list(self.database.animals.find(data))
        except Exception as e:
            #print("An error occured during the read ::", e)
            return ([], [])
        
    # Update CRUD function
    # data = dictionary of key/value pair(s) to find
    # mod = dictionary of key/value pair(s) to modify
    # Returns number of modified objects
    def update(self, data, mod):
        try:
            result = self.database.animals.update_many(data, {"$set": mod})
            return result.modified_count
        except Exception as e:
            #print("An error occured during the write ::", e)
            return 0
    
    # Delete CRUD function
    # data = dictionary of key/value pair(s)
    # Returns number of deleted objects
    def delete(self, data):
        try:
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        except Exception as e:
            #print("An error occured during the delete ::", e)
            return 0

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32398
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        