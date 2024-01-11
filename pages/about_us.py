import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#F8F9FA',  # Couleur de fond légère
}

image_style = {
    'width': '100%',  
    'max-width': '500px',  
    'height': 'auto',  
    'display': 'block',  
    'margin': '0 auto', 
}

layout = html.Div([
    html.Div([
        html.H1('About us', style={'textAlign': 'center',
                'color': '#670907', 'font-size': '2.5em'}),
    ], style=card_style),
    html.Br(),
    html.Div(style={'textAlign': 'center'}, children=[
        html.H4(["Nous sommes un groupe de 4 étudiantes, TISSANDIER Mathilde, MOUCHRIF Dounia, ABARKAN Suhaila et ROMAN Karina en master 1 du ",
                html.A("Cursus Master en Ingénierie (CMI) en Ingénierie Statistique et Informatique (ISI)",
                       href='https://formations.u-bordeaux.fr/#/details-formation?type=parcours-type&id=39693', target='_blank'),
                " à l'Université de Bordeaux. "]),
        html.H4(
            ["Nous réalisons un projet de visualisation sur les données de la SNCF."]),
        html.Br(),
        html.Img(src="/static/IMG/Groupe.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
    ]),
    html.Img(src="/static/IMG/gif.gif",
            style=image_style),
])
