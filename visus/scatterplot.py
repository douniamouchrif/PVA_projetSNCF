import pandas as pd
import plotly.express as px
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['projetSNCF']


def build_scatter(df):
    df['Mois'] = df['Mois'].dt.strftime('%Y-%m')

    fig = px.scatter(df, x='Mois', y='gravite_epsf',
                     title='Gravité moyenne par mois', color='gravite_epsf', size='gravite_epsf')
    fig.show()
