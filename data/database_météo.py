from pymongo import MongoClient
import requests

hostname = 'localhost'
port = 27017  # Default MongoDB port

# Create a MongoClient instance
client = MongoClient(hostname, port)

db = client['Météo']

def fetch_and_insert_data(db, collection_name, url, limit=100):
    collection = db[collection_name]
    offset = 0

    while True:
        payload = {'limit': limit, 'offset': offset}
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            data = response.json()

            # Select only the specified columns
            selected_data = [
                {
                    'date': entry['date'],
                    'non_reg': entry['nom_reg'],
                    'ff': entry['ff'],
                    'tc': entry['tc'],
                    'rr24': entry['rr24'],
                    'coordonnees': entry['coordonnees'],
                }
                for entry in data['results']
            ]

            collection.insert_many(selected_data)

            offset += len(data['results'])
            if len(data['results']) < limit:
                break

        else:
            print('Error fetching data:', response.status_code)
            break

url_météo = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records'
fetch_and_insert_data(db, "météo", url_météo)