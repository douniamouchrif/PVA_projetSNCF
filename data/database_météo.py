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

    def fetch_data_and_insert(offset):
        payload = {'limit': limit, 'offset': offset}
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            data = response.json()

            # Filter data for the period between 2015 and 2023
            filtered_data = []
            for entry in data['results']:
                date = entry.get('date')
                if date >= '2015-01-01' and date <= '2023-12-31':
                    filtered_data.append({
                        'date': entry.get('date'),
                        'non_reg': entry.get('non_reg'),
                        'ff': entry.get('ff'),
                        'tc': entry.get('tc'),
                        'rr24': entry.get('rr24'),
                        'coordonnees': entry.get('coordonnees'),
                    })

        print(f"Number of entries before filtering: {len(data['results'])}")
        print(f"Number of entries after filtering: {len(filtered_data)}")

        if len(filtered_data) == 0:
            print("No data meets the filtering conditions.")
            return

        collection.insert_many(filtered_data)

        if len(data['results']) < limit:
            return
        else:
            fetch_data_and_insert(offset + limit)

    fetch_data_and_insert(offset)



url_météo = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records'
fetch_and_insert_data(db, "météo", url_météo)