import plotly.graph_objects as go
import pandas as pd
from pymongo import MongoClient

###LES COULEURS C'EST PAS OUF MAIS ÇA MARCHE ENFIN 

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


#####CECI EST UN BROUILLON J'ESSAYAIS D'AJOUTER UN TRUC POUR SELECTIONNER LES ANNÉES

'''
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Connexion à MongoDB
hostname = 'localhost'
port = 27017
client = MongoClient(hostname, port)
db = client['projetSNCF']
cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {'date': {'$ne': None}}, {'niveau_gravite': 1, 'origine': 1, 'date': 1, '_id': 0})
df = pd.DataFrame(list(cursor))
print(df)
df = df['niveau_gravite', 'origine'].groupby(['niveau_gravite', 'origine']).size().reset_index(name='count')
print(df)

# Liste des années uniques dans votre DataFrame
years = df['annee'].unique()

# Création de l'application Dash
app = dash.Dash(__name__)

# Mise en page de l'application avec le dropdown
app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in years],
        value=years[0],  # Année par défaut
        multi=False,
        style={'width': '50%'}
    ),
    dcc.Graph(id='sunburst-chart'),
])

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
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees


# Callback pour mettre à jour le sunburst chart en fonction de l'année sélectionnée
@app.callback(
    Output('sunburst-chart', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_sunburst_chart(selected_year):
    # Filtrer les données en fonction de l'année sélectionnée
    filtered_df = df[df['annee'] == selected_year]
    
    # Grouper les données filtrées
    grouped_df = filtered_df.groupby(['niveau_gravite', 'origine']).size().reset_index(name='count')

    # Construire la hiérarchie des données
    df_all_trees = build_hierarchical_dataframe(grouped_df, levels, value_column)

    # Calculer la moyenne pour la couleur
    #average_score = grouped_df[color_columns[0]].sum() / grouped_df[color_columns[1]].sum()

    # Créer le graphique Sunburst
    fig = go.Figure(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        hovertemplate='<b>%{label} </b> <br> Count: %{value}<br> Success rate: %{color:.2f}',
        maxdepth=2
    ))

    # Mise à jour de la mise en page
    fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

'''