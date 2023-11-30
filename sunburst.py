import plotly.graph_objects as go
import pandas as pd
from pymongo import MongoClient

# Connexion à MongoDB
hostname = 'localhost'
port = 27017
client = MongoClient(hostname, port)
db = client['projetSNCF']
cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {'niveau_gravite': 1, 'origine': 1, '_id': 0})
df = pd.DataFrame(list(cursor))
df = df.groupby(['niveau_gravite', 'origine']).size().reset_index(name='count')

# Noms de colonnes et niveaux adaptés à votre ensemble de données
levels = ['origine', 'niveau_gravite']
value_column = 'count'

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum()
        print(dfg)
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        print(df_tree)
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'ACCIDENTS SNCF'
        df_tree['value'] = dfg[value_column]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='ACCIDENTS SNCF', parent='',
                              value=df[value_column].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees

df_all_trees = build_hierarchical_dataframe(df, levels, value_column)

marker_colors = ['blue', 'green', 'red', 'purple', 'yellow', 'pink', 'grey', 'orange', 'cyan', 'magenta', 'brown', 'teal', 'lime', 'indigo', 'maroon', 'olive', 'navy', 'aquamarine', 'orchid', 'slategray']
fig = go.Figure(go.Sunburst(
    labels=df_all_trees['id'],
    parents=df_all_trees['parent'],
    values=df_all_trees['value'],
    branchvalues='total',
    hovertemplate='<b>%{label} </b> <br> Count: %{value}',
    maxdepth=2,
    marker=dict(colors=marker_colors),
))
fig.update_layout(margin=dict(t=15, b=15, r=15, l=15))
fig.show()


'''hostname = 'localhost'
port = 27017
client = MongoClient(hostname, port)
db = client['projetSNCF']

def build_hierarchical_dataframe():
    cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {'niveau_gravite': 1, 'origine': 1, '_id': 0})
    df = pd.DataFrame(list(cursor))
    df = df.groupby(['niveau_gravite', 'origine']).size().reset_index(name='count')

    # Noms de colonnes et niveaux adaptés à votre ensemble de données
    levels = ['origine', 'niveau_gravite']
    value_column = 'count'
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum()
        print(dfg)
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        print(df_tree)
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'ACCIDENTS SNCF'
        df_tree['value'] = dfg[value_column]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='ACCIDENTS SNCF', parent='',
                              value=df[value_column].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees

def build_sunburst(df_all_trees=build_hierarchical_dataframe()):
    marker_colors = ['blue', 'green', 'red', 'purple', 'yellow', 'pink', 'grey', 'orange', 'cyan', 'magenta', 'brown', 'teal', 'lime', 'indigo', 'maroon', 'olive', 'navy', 'aquamarine', 'orchid', 'slategray']
    fig = go.Figure(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        hovertemplate='<b>%{label} </b> <br> Count: %{value}',
        maxdepth=2,
        marker=dict(colors=marker_colors),
    ))
    fig.update_layout(margin=dict(t=15, b=15, r=15, l=15))
    fig.show()
    return fig'''