""""
  must use 127.0.0.1 on the constructor on windows
  pip install pymongo

"""
from pymongo import MongoClient


class MongoDBConnection():
    """MongoDB Connection"""

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def print_mdb_collection(collection_name):
    for doc in collection_name.find():
        print(doc)


def main():
    mongo = MongoDBConnection()

    with mongo:
        # mongodb database; it all starts here
        db = mongo.connection.media

        # collection in database
        cd = db["cd"]

        # notice how easy these are to create and that they are "schemaless"
        # that is, the Python module defines the data structure in a dict,
        # rather than the database which just stores what it is told

        cd_ip = {"artist": "The Who", "Title": "By Numbers"}
        cd.insert_one(cd_ip)

        cd_ip = [{
            "artist": "Deep Purple",
            "Title": "Made In Japan",
            "name": "Andy"
        },
            {
            "artist": "Led Zeppelin",
            "Title": "House of the Holy",
                     "name": "Andy"
        }, {
            "artist": "Pink Floyd",
            "Title": "DSOM",
                     "name": "Andy"
        },
            {
            "artist": "Albert Hammond",
            "Title": "Free Electric Band",
                     "name": "Sam"
        }, {
            "artist": "Nilsson",
            "Title": "Without You",
                     "name": "Sam"
        }]

        cd.insert_many(cd_ip)

        print_mdb_collection(cd)

        # another collection
        collector = db["collector"]

        collector_ip = [{
            "name": "Andy",
            "preference": "Rock"
        }, {
            "name": "Sam",
            "preference": "Pop"
        }]
        collector.insert_many(collector_ip)

        print_mdb_collection(collector)

        # related data
        for name in collector.find():
            print(f'List for {name["name"]}')
            query = {"name": name["name"]}
            for a_cd in cd.find(query):
                print(f'{name["name"]} has collected {a_cd}')

        # start afresh next time?
        yorn = input("Drop data?")
        if yorn.upper() == 'Y':
            cd.drop()
            collector.drop()


if __name__ == "__main__":
    main()
