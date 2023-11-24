import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pymongo import MongoClient
from ipywidgets import interactive, IntRangeSlider
from IPython.display import display, clear_output

# Connexion à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client['projetSNCF']
collection = db['sncf1522']

# Récupération des données depuis MongoDB
cursor = collection.find({}, {'region': 1, 'origine': 1, 'niveau_gravite': 1, 'date': 1})
df = pd.DataFrame(list(cursor))

# Extraction de l'année à partir de la colonne de date
df['year'] = pd.to_datetime(df['date']).dt.year

# Conversion de la colonne 'niveau_gravite' en numérique
df['niveau_gravite'] = pd.to_numeric(df['niveau_gravite'], errors='coerce')

# Les 5 principales régions et types d'incidents avec le plus d'incidents
top_regions = df['region'].value_counts().nlargest(5).index
top_types = df['origine'].value_counts().nlargest(5).index

# Création d'un curseur interactif (range slider) pour sélectionner une plage d'années
years_range_slider = IntRangeSlider(
    value=[df['year'].min(), df['year'].max()],
    min=df['year'].min(),
    max=df['year'].max(),
    step=1,
    description='Années:',
    continuous_update=False,
    orientation='horizontal',
)

# Fonction de mise à jour du graphique en fonction de la plage d'années sélectionnée
def update_plot(years):
    selected_data = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]
    top_data = selected_data[selected_data['region'].isin(top_regions) & selected_data['origine'].isin(top_types)]

    mean_gravity_df = top_data.groupby(['region', 'origine'])['niveau_gravite'].mean().unstack()
    mean_gravity_df = mean_gravity_df[mean_gravity_df.sum().sort_values(ascending=False).index]
    mean_gravity_df = mean_gravity_df.loc[mean_gravity_df.sum(axis=1).sort_values(ascending=False).index]

    # Effacer la sortie précédente
    clear_output(wait=True)

    # Créer et afficher le nouveau graphique
    fig, ax = plt.subplots(figsize=(12, 8))
    mean_gravity_df.plot(kind='bar', ax=ax)
    ax.set_xlabel('Région')
    ax.set_ylabel('Gravité Moyenne')
    ax.set_title('Gravité Moyenne des 5 Principaux Types d\'Incidents dans les 5 Principales Régions')
    ax.legend(title='Type d\'Incident', bbox_to_anchor=(1, 1), loc='upper left')

# Creation du graphique interactif
interactive_plot = interactive(update_plot, years=years_range_slider)

display(interactive_plot)
