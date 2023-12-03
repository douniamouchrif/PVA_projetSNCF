import plotly.express as px


def build_scatter23(df):
    df['Mois'] = df['Mois'].dt.strftime('%Y-%m')
    fig = px.scatter(df, x='Mois', y='gravite_epsf',
                     title='Gravité moyenne par mois', color='gravite_epsf', size='gravite_epsf')
    return fig


def build_scatter1522(df):
    df['Mois'] = df['Mois'].dt.strftime('%Y-%m')
    fig = px.scatter(df, x='Mois', y='niveau_gravite',
                     title=f'Gravité moyenne par mois', color='niveau_gravite', size='niveau_gravite')
    return fig
