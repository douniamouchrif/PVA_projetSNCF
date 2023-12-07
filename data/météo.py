from datetime import datetime
import requests
from pymongo import MongoClient

hostname = 'localhost'
port = 27017
client = MongoClient(hostname, port)
db = client['Météo']

result23 = db.sncf23.find()
dates_list_23 = [entry["date"] for entry in result23]
result1522 = db.find1522.find()
dates_list_1522 = [entry["date"] for entry in result1522]

url='https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?select=date%2Cnom_reg%2Cff%2Ctc%2Crr24%2Ccoordonnees&where=nom_reg%20%3D%20%27%C3%8Ele-de-France%27%20or%20nom_reg%20%3D%20%27Auvergne-Rh%C3%B4ne-Alpes%27%20or%20nom_reg%20%3D%27Grand%20Est%27%20or%20%20nom_reg%20%3D%20%27Hauts-de-France%27%20or%20nom_reg%20%3D%20%27Occitanie%27%20or%20nom_reg%20%3D%20%27Nouvelle-Aquitaine%27%20%20or%20nom_reg%20%3D%20%22Provence-Alpes-C%C3%B4te%20d%27Azur%22%20or%20nom_reg%20%3D%20%27Centre-Val%20de%20Loire%27%20%20or%20nom_reg%3D%27Bourgogne-Franche-Comt%C3%A9%27%20or%20nom_reg%3D%27Bretagne%27%20or%20%20nom_reg%20%3D%20%27Pays%20de%20la%20Loire%27%20or%20nom_reg%3D%27Normandie%27'

def fetch_and_insert_data(db, collection_name, url, dates_list_23, dates_list_1522, limit=100):
    collection = db[collection_name]
    offset = 0

    def fetch_data_and_insert(offset):
        payload = {'limit': limit, 'offset': offset}
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])

            for entry in records:
                iso_date = entry.get("date")
                if iso_date:
                    formatted_date = datetime.fromisoformat(iso_date).strftime("%Y-%m-%d")
                    if formatted_date in dates_list_23 or formatted_date in dates_list_1522:
                        collection.insert_one(entry)
                        print(f"Inserted: {entry}")

            if len(records) < limit:
                print("Finished fetching and inserting data.")
                return
            else:
                fetch_data_and_insert(offset + limit)

    fetch_data_and_insert(offset)

# Exécution de la fonction avec des messages de débogage
fetch_and_insert_data(db, "météo", url, dates_list_23, dates_list_1522)
