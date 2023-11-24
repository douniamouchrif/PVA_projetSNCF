import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client['projetSNCF']   
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

# Gestion des couleurs
sns.set_palette("husl")
ax = mean_gravity_df.plot(kind='bar', figsize=(12, 8))
ax.set_xlabel('Région')
ax.set_ylabel('Gravité Moyenne')
ax.set_title('Gravité Moyenne des 5 Principaux Types d\'Incidents dans les 5 Principales Régions')

ax.legend(title='Type d\'Incident', bbox_to_anchor=(1, 1), loc='upper left')

plt.show()