from pymongo import MongoClient

def get_cnx_database(CONNECTION_CONF = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1", DATABASE_NAME = "facebook"):
    # Create a connection using MongoClient
    cnx = MongoClient(CONNECTION_CONF)
    return cnx[DATABASE_NAME]