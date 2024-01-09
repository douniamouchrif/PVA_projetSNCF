import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', location="sidebar", external_stylesheets=[
                   dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Style du cadre
card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#F8F9FA',  # Couleur de fond légère
}


layout = html.Div(style={'color': 'black', 'min-height': '100vh'}, children=[
    html.Div([
        html.H1('Home', style={'textAlign': 'center',
                'color': '#670907', 'font-size': '2.5em'}),
    ], style=card_style),
    html.Br(),
    html.H2("Bienvenue sur la page d'accueil !",
            style={'textAlign': 'center', 'fontSize': '3.0em'}),
    html.Br(),
    html.Div(style={'color': 'black'}, children=[
        html.H4(
            'Mesdames et Messieurs, bonjour et bienvenue à bord de notre Dashboard en direction du 20/20. '
            'Au départ de la page Home, notre Dashboard desservira la page Visualisations et la page About us, son terminus.',
            style={'textAlign': 'center', 'fontSize': '1.75em'}),
        html.H4(
            'Nous vous souhaitons à toutes et à tous une agréable expérience. Attention au départ !',
            style={'textAlign': 'center', 'fontSize': '1.75em'}),
        html.Br(),
        html.Img(src='/static/IMG/gare.png', style={'width': '20%', 'display': 'block',
                 'margin-left': 'auto', 'margin-right': 'auto', 'margin-bottom': '20px'}),
        html.Br(),
        html.H5("Pour la récupération des données, nous avons mis en place une utilisation de l'outil MongoDB "
                "avec l'API afin d'assurer une mise à jour régulière et une précision maximale. Les données sont extraites "
                "à partir du site officiel de la SNCF et sont traitées de manière à fournir des informations "
                "pertinentes et à jour.", style={'fontSize': '1.5em'}),
        html.H5("Nous espérons offrir la meilleure expérience possible, et c'est pourquoi nous utilisons 4 bases de données :", style={
                'fontSize': '1.5em'}),
        html.Div(style={'display': 'flex', 'flexDirection': 'column', 'fontSize': '1.5em'}, children=[
            html.Li(html.A("Incidents de sécurité (Evénements de sécurité remarquables - ESR) de janvier 2015 à décembre 2022",
                    href='https://data.sncf.com/explore/dataset/incidents-securite/table/?sort=date', target='_blank')),
            html.Li(html.A("Incidents de sécurité (EPSF) depuis janvier 2023", href='https://data.sncf.com/explore/dataset/incidents-de-securite-epsf/table/?sort=date&calendarview=month&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoiZ3Jhdml0ZV9lcHNmIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ExMDA2QiJ9XSwieEF4aXMiOiJkYXRlIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJpbmNpZGVudHMtZGUtc2VjdXJpdGUtZXBzZiIsIm9wdGlvbnMiOnsic29ydCI6ImRhdGUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D', target='_blank')),
            html.Li(html.A("Liste des lignes électrifiées",
                    href='https://data.sncf.com/explore/dataset/liste-des-lignes-electrifiees/table/', target='_blank')),
            html.Li(html.A("Lignes par type",
                    href='https://data.sncf.com/explore/dataset/lignes-par-type/table/', target='_blank')),
            html.Li(html.A("Lignes par région administrative",
                    href='https://data.sncf.com/explore/dataset/lignes-par-region-administrative/table/', target='_blank'))
        ])
    ])
])
