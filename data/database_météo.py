import requests
from connect import client

db = client['Météo']

# Pour le moment nous ne pouvons récupérer que 10 000 données car le site nous bloque les données suivantes
def fetch_and_insert_data(db, collection_name, url, limit=100):
    collection = db[collection_name]
    offset = 0

    while True:
        payload = {'limit': limit, 'offset': offset}
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            data = response.json()

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