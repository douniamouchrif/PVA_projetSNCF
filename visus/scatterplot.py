import pandas as pd
import plotly.express as px
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['projetSNCF']


def get_data():
    result = db.sncf23.find({
        'gravite_epsf': {'$ne': None},
        'date': {'$gte': '2023-01-01', '$lte': '2023-08-31'}
    }, {'gravite_epsf': 1, 'date': 1})

    df = pd.DataFrame(result)
    df['date'] = pd.to_datetime(df['date'])
    df['Mois'] = df['date'].dt.to_period('M')
    grouped_data = df.groupby('Mois')['gravite_epsf'].mean().reset_index()

    return grouped_data


df = get_data()
df['Mois'] = df['Mois'].dt.strftime('%Y-%m')

fig = px.scatter(df, x='Mois', y='gravite_epsf',
                 title='Gravité moyenne par mois', color='gravite_epsf', size='gravite_epsf')
fig.show()
