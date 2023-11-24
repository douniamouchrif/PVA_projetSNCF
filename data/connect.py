from pymongo import MongoClient

hostname = 'localhost'
port = 27017  # Default MongoDB port
client = MongoClient(hostname, port)
db = client['projetSNCF']