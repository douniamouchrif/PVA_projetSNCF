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

df['year'] = pd.to_datetime(df['date']).dt.year

# Convert 'niveau_gravite' column to numeric
df['niveau_gravite'] = pd.to_numeric(df['niveau_gravite'], errors='coerce')

# Get the top 5 regions and incident types by the most incidents
top_regions = df['region'].value_counts().nlargest(5).index
top_types = df['origine'].value_counts().nlargest(5).index

# Create a RangeSlider for selecting years
years_range_slider = IntRangeSlider(
    value=[df['year'].min(), df['year'].max()],
    min=df['year'].min(),
    max=df['year'].max(),
    step=1,
    description='Years:',
    continuous_update=False,
    orientation='horizontal',
)

# Function to update the plot based on the selected years
def update_plot(years):
    selected_data = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]
    top_data = selected_data[selected_data['region'].isin(top_regions) & selected_data['origine'].isin(top_types)]

    mean_gravity_df = top_data.groupby(['region', 'origine'])['niveau_gravite'].mean().unstack()
    mean_gravity_df = mean_gravity_df[mean_gravity_df.sum().sort_values(ascending=False).index]
    mean_gravity_df = mean_gravity_df.loc[mean_gravity_df.sum(axis=1).sort_values(ascending=False).index]

    # Clear the previous output
    clear_output(wait=True)

    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    mean_gravity_df.plot(kind='bar', ax=ax)
    ax.set_xlabel('Region')
    ax.set_ylabel('Mean Gravity')
    ax.set_title('Mean Gravity of Top 5 Incident Types in Top 5 Regions')
    ax.legend(title='Incident Type', bbox_to_anchor=(1, 1), loc='upper left')

# Create an interactive widget
interactive_plot = interactive(update_plot, years=years_range_slider)

# Display the interactive widget
display(interactive_plot)
