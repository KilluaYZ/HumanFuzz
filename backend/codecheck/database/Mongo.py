import pymongo
import config
from codecheck.utils.Logger import logger
from flask import current_app
import config

MONGO_HOST = config.MONGO_HOST
MONGO_PORT = config.MONGO_PORT
MONGO_DB = config.MONGO_DB
MONGO_USER = config.MONGO_USER
MONGO_PASSWORD = config.MONGO_PASSWORD

class Mongo:
    def __init__(self, 
                 host=MONGO_HOST, 
                 port=MONGO_PORT, 
                 database=MONGO_DB,
                 user=MONGO_USER,
                 password=MONGO_PASSWORD
                 ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.client = None
    
    def get_client(self) -> pymongo.MongoClient:
        try:
            if self.client is None:
                if self.password is not None and self.user is not None:
                    self.client = pymongo.MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/')
                else:
                    self.client = pymongo.MongoClient(f'mongodb://{self.host}:{self.port}/')
                logger.logger.info(f"与MongoDB {self.host}:{self.port} 建立连接")
        except Exception as e:
            logger.logger.error(f"与MongoDB {self.host}:{self.port} 建立连接失败")
            logger.logger.error(e)
        return self.client

    def get_db(self):
        return self.get_client().get_database(self.database)

    def get_collection(self, collection: str):
        return self.get_db().get_collection(collection)

    def insert_one(self, collection: str, document: dict, session=None):
        collection = self.get_collection(collection)
        return collection.insert_one(document, session=session)

    def insert_many(self, collection: str, document: list, session=None):
        collection = self.get_collection(collection)
        return collection.insert_many(document, session=session)

    def find_one(self, collection: str, query: dict):
        collection = self.get_collection(collection)
        return collection.find_one(query)

    def find(self, collection: str, query: dict):
        collection = self.get_collection(collection)
        return collection.find(query)

    def update_one(self, collection: str, query: dict, value: dict, session=None):
        collection = self.get_collection(collection)
        return collection.update_one(query, value, session=session)

    def delete_one(self, collection: str, query: dict, session=None):
        collection = self.get_collection(collection)
        return collection.delete_one(query, session=session)
    def delete_many(self, collection: str, query: dict, session=None):
        collection = self.get_collection(collection)
        return collection.delete_many(query, session=session)

    def get_session(self):
        self.client = self.get_client()
        return self.client.start_session(causal_consistency=True)

