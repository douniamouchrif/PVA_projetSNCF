import pandas as pd
from connect import db


def get_data_barplot_2023():
    # Connexion à la base de données MongoDB  
    collection = db['sncf23']

    # Récupération des données depuis MongoDB
    cursor = collection.find({}, {'region': 1, 'origine': 1, 'gravite_epsf': 1})
    df = pd.DataFrame(list(cursor))

    # Les 5 principales régions et types d'incidents avec le plus d'incidents
    top_regions = df['region'].value_counts().nlargest(5).index
    top_types = df['origine'].value_counts().nlargest(5).index

    # Les données pour les principales régions et types
    top_data = df[df['region'].isin(top_regions) & df['origine'].isin(top_types)]

    # Nouveau dataframe avec la gravité moyenne pour chaque région et type d'incident
    mean_gravity_df = top_data.groupby(['region', 'origine'])['gravite_epsf'].mean().unstack()

    # Trier les données par le nombre d'incidents pour les régions et les types d'incidents
    mean_gravity_df = mean_gravity_df[mean_gravity_df.sum().sort_values(ascending=False).index]
    mean_gravity_df = mean_gravity_df.loc[mean_gravity_df.sum(axis=1).sort_values(ascending=False).index]

    return mean_gravity_df