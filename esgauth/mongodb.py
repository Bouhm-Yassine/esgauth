from pymongo import MongoClient

class MongoDB:
    _instance = None

    def __new__(cls, mongo_uri):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)

            cls._instance.client = MongoClient(mongo_uri)
            cls._instance.db = cls._instance.client.get_default_database()

        return cls._instance
    

    @classmethod
    def get_user(cls, query):
        return cls._instance.db.users.find_one(query)
