import pandas as pd
from pymongo import MongoClient
import plotly.express as px

def filter_data(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Conversion en datetime
    df['year'] = df['date'].dt.strftime('%Y')

    # Filtrage des lignes avec des valeurs NaN dans les colonnes 'year', 'origine', et 'type_event'
    df_filtered = df.dropna(subset=['year', 'origine', 'type_event'])

    return df_filtered

def create_cumulative_line_plot(data):
    # Prétraitement des données
    df_filtered = filter_data(data)
    
    # Grouping by year and origin, counting the number of events
    df_grouped = df_filtered.groupby(['year', 'origine']).size().reset_index(name='count')

    # Adding a new column for cumulative count starting from 2015
    df_grouped['cumulative_count'] = df_grouped.groupby('origine')['count'].cumsum()

    # Creating cumulative line plot
    fig = px.line(df_grouped, x='year', y='cumulative_count', color='origine',
                  labels={'cumulative_count': 'Nombre cumulatif d\'événements', 'year': 'Année'},
                  title='Évolution du nombre cumulatif d\'événements par origine au fil des années')
    
    fig.update_layout(
        title_font=dict(size=24),
        xaxis=dict(
            title=dict(text='Années', font=dict(size=18)),
            tickfont=dict(size=18),
        ),
        yaxis=dict(title=dict(text='Nombre cumulatif d\'événements', font=dict(size=22)),
                   tickfont=dict(size=18),),
        legend=dict(
            x=1.02,
            y=0.5,
            traceorder='normal',
            font=dict(size=16),
            bgcolor='rgba(255, 255, 255, 0.5)',
        )
    )
    
    fig.show()

# Example usage
client = MongoClient('localhost', 27017)
db = client['projetSNCF']
cursor = db.sncf1522.find({})
data = list(cursor)

create_cumulative_line_plot(data)

