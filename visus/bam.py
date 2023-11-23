import plotly.express as px
from pymongo import MongoClient
import pandas as pd

# Connexion à MongoDB
client = MongoClient('localhost', 27017)
db = client['projetSNCF']
collection = db["sncf1522"]

# Récupération des données depuis MongoDB
cursor = collection.find({})
data = list(cursor)

# Prétraitement des données
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(
    df['date'], errors='coerce')  # Conversion en datetime
df['year'] = df['date'].dt.strftime('%Y')

# Filtrage des lignes avec des valeurs NaN dans les colonnes 'year' et 'origine'
df_filtered = df.dropna(subset=['year', 'origine'])

# Création du graphique en boîtes avec Plotly Express et menu déroulant
fig = px.box(df_filtered, x='year', y=df_filtered.groupby('year').cumcount(), labels={'y': 'Nombre d incidents'},
             title='Nombre d incidents par année',
             category_orders={'year': sorted(df_filtered['year'].unique())},
             animation_group='origine')

fig.update_layout(
    title_font=dict(size=24),  # Modifiez la taille du titre principal
    # Modifiez la taille du titre de l'axe des x
    xaxis=dict(
        # Modifiez la taille du titre de l'axe des x
        title=dict(text='Années', font=dict(size=18)),
        # Modifiez la taille des valeurs sur l'axe des x
        tickfont=dict(size=18),
    ),
    # Modifiez la taille du titre de l'axe des y
    yaxis=dict(title=dict(text='Nombre d incidents', font=dict(size=22)),
               tickfont=dict(size=18),),
)


# Affichage du graphique dans un navigateur web
fig.show()
