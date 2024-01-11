from connect import db
import pandas as pd

collection_sncf1522 = db['sncf1522']
cursor_sncf1522 = collection_sncf1522.find()
df_sncf1522 = pd.DataFrame(list(cursor_sncf1522))

correspondance_regions = {
    "AURA": "Auvergne-Rhône-Alpes",
    "OCC": "Occitanie",
    "IDF": "Île-de-France",
    "GE": "Grand Est",
    "NAQ": "Nouvelle-Aquitaine",
    "BFC": "Bourgogne-Franche-Comté",
    "PCA": "Provence-Alpes-Côte d'Azur",
    "PACA": "Provence-Alpes-Côte d'Azur",
    "HDF": "Hauts-de-France",
    "RA": "Auvergne-Rhône-Alpes",
    "PDL": "Pays de la Loire",
    "NMD": "Normandie",
    "IdF": "Île-de-France",
    "CVL": "Centre-Val de Loire",
    "PRG": "Pays de la Loire",
    "PE": "Provence-Alpes-Côte d'Azur",
    "LR": "Occitanie",
    "NPC": "Nord-pas-de-Calais",
    "PAK": "Provence-Alpes-Côte d'Azur",
    "PN": "Provence-Alpes-Côte d'Azur",
    "BRE": "Bretagne",
    "PSE": "Pays de la Loire",
    "AUV": "Auvergne-Rhône-Alpes",
    "LOR": "Grand Est",
    "PSL": "Île-de-France",
    "CEN": "Centre-Val de Loire",
    "ALP": "Provence-Alpes-Côte d'Azur",
    "AL": "Provence-Alpes-Côte d'Azur",
    "NOR": "Normandie",
    "MPY": "Occitanie",
    "CA": "Corse",
    "HdF": "Hauts-de-France",
    "PIC": "Picardie",
    "BZH": "Bretagne",
    "LM": "Bretagne",
    "AN": "Auvergne-Rhône-Alpes",
    "BR": "Bretagne",
    "Naq": "Nouvelle-Aquitaine",
    "LIM": "Nouvelle-Aquitaine",
    "CE": "Centre-Val de Loire",
    "GEST": "Grand Est",
    "NAq": "Nouvelle-Aquitaine",
    "ETR": "Étranger",
    "Poitou-Charentes": "Nouvelle-Aquitaine",
    "Idf": "Île-de-France",
    "aRF": "Auvergne-Rhône-Alpes",
    "BDx": "Nouvelle-Aquitaine",
    "RS": "Étranger",
    "PL": "Pays de la Loire",
    "Espagne": "Étranger",
    "NPDC": "Nord-pas-de-Calais",
    "APC": "Auvergne-Rhône-Alpes",
    "Occ": "Occitanie",
    "0.7142857142857143": "Étranger",
    "Hdf": "Hauts-de-France",
    "PiC": "Picardie",
    "VP": "Étranger"
}

df_sncf1522['region'] = df_sncf1522['region'].map(correspondance_regions)

for index, row in df_sncf1522.iterrows():
    collection_sncf1522.update_one({'_id': row['_id']}, {'$set': {'region': row['region']}})