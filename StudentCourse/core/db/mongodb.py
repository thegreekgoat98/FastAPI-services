from pymongo import MongoClient
from script.config import DBConf

db_obj=DBConf()

mongo_uri=DBConf.MONGO_URI
mongo_dbname=DBConf.MONGO_DBNAME
mongo_collname=DBConf.MONGO_COLLNAME
class Mongo:
    client = MongoClient(mongo_uri)
    db = client[mongo_dbname]
    myDB = db[mongo_collname]