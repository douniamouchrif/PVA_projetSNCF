import pandas as pd
from data.connect import db


def get_data_barplot_2023():
    # Connexion à la base de données MongoDB
    collection = db['sncf23']

    # Récupération des données depuis MongoDB
    cursor = collection.find(
        {}, {'region': 1, 'origine': 1, 'gravite_epsf': 1})
    df = pd.DataFrame(list(cursor))

    # Les 5 principales régions et types d'incidents avec le plus d'incidents
    top_regions = df['region'].value_counts().nlargest(5).index
    top_types = df['origine'].value_counts().nlargest(5).index

    # Les données pour les principales régions et types
    top_data = df[df['region'].isin(
        top_regions) & df['origine'].isin(top_types)]

    # Nouveau dataframe avec la gravité moyenne pour chaque région et type d'incident
    mean_gravity_df = top_data.groupby(['region', 'origine'])[
        'gravite_epsf'].mean().unstack()

    # Trier les données par le nombre d'incidents pour les régions et les types d'incidents
    mean_gravity_df = mean_gravity_df[mean_gravity_df.sum(
    ).sort_values(ascending=False).index]
    mean_gravity_df = mean_gravity_df.loc[mean_gravity_df.sum(
        axis=1).sort_values(ascending=False).index]

    return mean_gravity_df


def get_data_sunburst():
    cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {
                              'niveau_gravite': 1, 'origine': 1, '_id': 0})
    df = pd.DataFrame(list(cursor))
    df = df.groupby(['niveau_gravite', 'origine']
                    ).size().reset_index(name='count')
    # Noms de colonnes et niveaux adaptés à votre ensemble de données
    levels = ['origine', 'niveau_gravite']
    value_column = 'count'
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum(numeric_only=True)
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'ACCIDENTS SNCF'
        df_tree['value'] = dfg[value_column]
        df_all_trees = pd.concat([df_all_trees, df_tree], ignore_index=True)
    total = pd.Series(dict(id='ACCIDENTS SNCF', parent='',
                      value=df[value_column].sum()))
    df_all_trees = pd.concat([df_all_trees, total], ignore_index=True)
    return df_all_trees


def get_data_scatterplot():
    result = db.sncf23.find()
    df = pd.DataFrame(result)
    df['date'] = pd.to_datetime(df['date'])
    df['Mois'] = df['date'].dt.to_period('M')
    grouped_data = df.groupby('Mois')['gravite_epsf'].mean().reset_index()
    return grouped_data

def get_data_boxplot():
    result = db.sncf1522.find()
    df = pd.DataFrame(result)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Conversion en datetime
    df['year'] = df['date'].dt.strftime('%Y')

    # Filtrage des lignes avec des valeurs NaN dans les colonnes 'year' et 'origine'
    df_filtered = df.dropna(subset=['year', 'origine'])

    return df_filtered

def get_data_lineplot():
    result = db.sncf1522.find()
    df = pd.DataFrame(result)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Conversion en datetime
    df['year'] = df['date'].dt.strftime('%Y')
    df_filtered = df.dropna(subset=['year', 'origine', 'type_event'])

    return df_filtered