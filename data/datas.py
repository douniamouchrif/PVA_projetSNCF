from pymongo import MongoClient

# Provide the connection details
hostname = 'localhost'
port = 27017  # Default MongoDB port

# Create a MongoClient instance
client = MongoClient(hostname, port)

db = client['projetSNCF']  # projetSNCF = database de notre projet
db

collection23 = db["sncf23"]  # sncf23 = une des collections
url23 = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/incidents-de-securite-epsf/records'
limit = 100
offset = 0
'''
while True:
    payload = {'limit': limit, 'offset': offset}
    response = requests.get(url23, params=payload)

    if response.status_code == 200:
        data = response.json()
        collection23.insert_many(data['results'])
        if len(data['results']) < limit:
            break
        else:
            offset += limit
'''

collection1522 = db["sncf1522"]
url1522 = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/incidents-securite/records'
limit = 100
offset = 0
'''
while True:
    payload = {'limit': limit, 'offset': offset}
    response = requests.get(url1522, params=payload)

    if response.status_code == 200:
        data = response.json()
        collection1522.insert_many(data['results'])
        if len(data['results']) < limit:
            break
        else:
            offset += limit
'''

collectionLigneE = db["sncfLigneE"]
urlLigneE = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/liste-des-lignes-electrifiees/records'
limit = 100
offset = 0
'''
while True:
    payload = {'limit': limit, 'offset': offset}
    response = requests.get(urlLigneE, params=payload)

    if response.status_code == 200:
        data = response.json()
        collectionLigneE.insert_many(data['results'])
        if len(data['results']) < limit:
            break
        else:
            offset += limit
'''

collection_l_admin = db["sncf_l_admin"]
url_l_admin = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/lignes-par-region-administrative/records'
limit = 100
offset = 0
'''
while True:
    payload = {'limit': limit, 'offset': offset}
    response = requests.get(url_l_admin, params=payload)

    if response.status_code == 200:
        data = response.json()
        collection_l_admin.insert_many(data['results'])
        if len(data['results']) < limit:
            break
        else:
            offset += limit
'''

collectionLigneT = db["sncfLigneT"]
urlLigneT = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/lignes-par-type/records'
limit = 100
offset = 0
'''
while True:
    payload = {'limit': limit, 'offset': offset}
    response = requests.get(urlLigneT, params=payload)

    if response.status_code == 200:
        data = response.json()
        collectionLigneT.insert_many(data['results'])
        if len(data['results']) < limit:
            break
        else:
            offset += limit
'''
