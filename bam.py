import data.database
import plotly.graph_objects as go
import plotly.express as px
from pymongo import MongoClient
import pandas as pd

def filter_data(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Conversion en datetime
    df['year'] = df['date'].dt.strftime('%Y')

    # Filtrage des lignes avec des valeurs NaN dans les colonnes 'year' et 'origine'
    df_filtered = df.dropna(subset=['year', 'origine'])

    return df_filtered

client = MongoClient('localhost', 27017)
db = client['projetSNCF']
cursor = db.sncf1522.find({})
data = list(cursor)

# Prétraitement des données
df_filtered = filter_data(data)
fig = px.box(df_filtered, x='year', y=df_filtered.groupby('year').cumcount(), labels={'y': 'Nombre d incidents'},
                 title='Nombre d incidents par année',
                 category_orders={'year': sorted(df_filtered['year'].unique())},
                 animation_group='origine')
fig.add_trace(go.Scatter(
        x=['2019', '2019'],
        y=[0, df_filtered.groupby('year').cumcount().max() + 1],
        mode="lines",
        line=dict(color="red", width=2, dash='dash'),
        showlegend=True,  # Afficher la légende pour cette trace
        name='Début de la crise du COVID-19'
))
fig.update_layout(
        title_font=dict(size=24),
        xaxis=dict(
            title=dict(text='Années', font=dict(size=18)),
            tickfont=dict(size=18),
        ),
        yaxis=dict(title=dict(text='Nombre d incidents', font=dict(size=22)),
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