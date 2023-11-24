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

# Get the top 5 regions and incident types by the most incidents
top_regions = df['region'].value_counts().nlargest(5).index
top_types = df['origine'].value_counts().nlargest(5).index

# Filter data for the top regions and types
top_data = df[df['region'].isin(top_regions) & df['origine'].isin(top_types)]

# Create a new dataframe with mean gravity for each region and incident type
mean_gravity_df = top_data.groupby(['region', 'origine'])['gravite_epsf'].mean().unstack()

# Sort data by the most incidents for both regions and incident types
mean_gravity_df = mean_gravity_df[mean_gravity_df.sum().sort_values(ascending=False).index]
mean_gravity_df = mean_gravity_df.loc[mean_gravity_df.sum(axis=1).sort_values(ascending=False).index]

# Plotting using Seaborn for better color handling
sns.set_palette("husl")
ax = mean_gravity_df.plot(kind='bar', figsize=(12, 8))
ax.set_xlabel('Region')
ax.set_ylabel('Mean Gravity')
ax.set_title('Mean Gravity of Top 5 Incident Types in Top 5 Regions')

# Display legend outside the plot
ax.legend(title='Incident Type', bbox_to_anchor=(1, 1), loc='upper left')

plt.show()
