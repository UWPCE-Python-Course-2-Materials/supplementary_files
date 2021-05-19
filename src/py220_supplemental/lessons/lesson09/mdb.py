from pymongo import MongoClient


class MongoDBConnectionManager:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


# connecting with a localhost
with MongoDBConnectionManager("localhost", 27017) as mongo:
    collection = mongo.connection.SampleDb.test
    data = collection.find({"_id": 1})
    print(data.get("name"))
