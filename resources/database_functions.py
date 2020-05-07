import pymongo

def insert_many_objects_to_mongo(list_of_objects, connection_string, database, collection):
    '''
    Inserts all dictionaries in list of objects to mongodb collection
    '''
    try:
        #establish connection
        mng_client = pymongo.MongoClient(connection_string)
        mng_db = mng_client[database] 
        db_cm = mng_db[collection]
        
        #insert
        db_cm.insert_many(list_of_objects)

        #close connection
        mng_client.close()
    except:
        print(traceback.format_exc())
