import requests
from connect import db

url_SNCF = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/'

def fetch_and_insert_data(db, collection_name, url, limit=100):
    collection = db[collection_name]
    offset = 0

    def fetch_data_and_insert(offset):
        payload = {'limit': limit, 'offset': offset}
        response = requests.get(url, params=payload)

        if response.status_code == 200:
            data = response.json()
            collection.insert_many(data['results'])
            if len(data['results']) < limit:
                return
            else:
                fetch_data_and_insert(offset + limit)

    fetch_data_and_insert(offset)

url23 = url_SNCF + 'incidents-de-securite-epsf/records'
fetch_and_insert_data(db, "sncf23", url23)

url1522 = url_SNCF + 'incidents-securite/records'
fetch_and_insert_data(db, "sncf1522", url1522)

urlLigneE = url_SNCF + 'liste-des-lignes-electrifiees/records'
fetch_and_insert_data(db, "sncfLigneE", urlLigneE)

url_l_admin = url_SNCF + 'lignes-par-region-administrative/records'
fetch_and_insert_data(db, "sncf_l_admin", url_l_admin)

urlLigneT = url_SNCF + 'lignes-par-type/records'
fetch_and_insert_data(db, "sncfLigneT", urlLigneT)