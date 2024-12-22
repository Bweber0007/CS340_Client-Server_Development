from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

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
        PORT = 32892
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary 
                return result.acknowledged # boolean value of insert result
            except:
                return False # return false if could not insert
        else:
            raise Exception("Nothing to save, because data parameter is empty") # throws exception if no data

# Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                result = self.database.animals.find(query) # result value is a cursor
                return list(result) # change cursor value to a list
            except:
                return [] # returns an empty list if no result found
        else:
            raise Exception("Empty query") # throws exception if no query
            
    
# Method for updating document(s) in the database
    def update(self, query, data, updateOne):
        try:
            if updateOne is True:
                result = self.database.animals.update_one(query, data) # updates a single document matching the query with data
                return result.modified_count # returns 1 since single document updated
            else:
                result = self.database.animals.update_many(query, data) # updates multiple documents matching the query with data
                return result.modified_count # returns count of documents modified               
        # catches errors and returns 0 documents updated
        except:
            print("failed to update") 
            return 0
        
# Method for deleting document(s) in the database
    def delete(self, query, deleteOne):
        try:
            if deleteOne is True:
                result = self.database.animals.delete_one(query) # deletes a single document matching the query
                return result.deleted_count # returns 1 since single document deleted
            else:
                result = self.database.animals.delete_many(query) # deletes multiple documents matching the query
                return result.deleted_count # returns number of documents deleted
        # catches errors and returns 0 documents deleted
        except:
            print("failed to delete")
            return 0
        