import requests
from connect import db

url_SNCF = 'https://data.sncf.com/api/explore/v2.1/catalog/datasets/'
url_meteo = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/'

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

#url23 = url_SNCF + 'incidents-de-securite-epsf/records'
#fetch_and_insert_data(db, "sncf23", url23)

#url1522 = url_SNCF + 'incidents-securite/records'
#fetch_and_insert_data(db, "sncf1522", url1522)

urlLigneE = url_SNCF + 'liste-des-lignes-electrifiees/records'
fetch_and_insert_data(db, "sncfLigneE", urlLigneE)

url_l_admin = url_SNCF + 'lignes-par-region-administrative/records'
fetch_and_insert_data(db, "sncf_l_admin", url_l_admin)

urlLigneT = url_SNCF + 'lignes-par-type/records'
fetch_and_insert_data(db, "sncfLigneT", urlLigneT)

departements=['Gironde','Aube','Bouches-du-Rhône','Drôme','Finistère','Vienne','Alpes-Maritimes','Essonne','Haute-Garonne','Indre-et-Loire','Lot','Marne','Morbihan','Nord','Rhône',"Côtes-d'Armor",'Haut-Rhin','Haute-Corse','Hautes-Pyrénées','Ille-et-Vilaine','Loire-Atlantique','Cher','Haute-Loire','Haute-Vienne','Bas-Rhin','Charente-Maritime','Hérault','Ariège','Seine-Maritime','Puy-de-Dôme','Var','Pyrénées-Orientales','Somme','Aveyron','Meurthe-et-Moselle',"Côte-d'Or",'Hautes-Alpes','Manche','Landes','Orne','Calvados']
années = ['15','16','17','18','19','20','21','22','23']
for année in années :
    for departement in departements:
        url_météo = f"{url_meteo}donnees-synop-essentielles-omm/records?refine=date%3A%2220{année}%22&refine=nom_dept%3A%22{departement}%22"
        fetch_and_insert_data(db, "météo", url_météo)
