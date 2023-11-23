from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)

# Définir les options pour les visualisations
visualisations = {f'vis{i}': f'Visualisation {i}' for i in range(1, 9)}

# Définir les questions
questions = [
    "Le nombre d’incidents varie-t-il drastiquement d’une année à l’autre ?",
    "Comment les causes d’incidents ont-elles évolué au cours de ces 8 dernières années?",
    "Comment le nombre d’incidents par gravité a-t-il évolué ces 8 dernières années ? Quelles sont les principales origines des incidents pour une gravité choisie ?",
    "Quelles sont les causes des accidents les plus récurrentes ?",
    "Est-ce que les régions les plus fréquentées sont celles où se produisent le plus d’incidents ? Pour chaque région, quelle est la cause d’incidents qui atteint le plus grand niveau de gravité ?",
    "Quelles sont les lignes les plus impactées par les incidents et que peut-on en déduire sur leur dangerosité : s’améliorent-elles ou se dégradent-elles avec le temps ?",
    "Pourquoi y’a-t-il plus de lignes classiques que de lignes électrifiées ?",
    "Comment des conditions météorologiques particulières, comme le vent et la température, peuvent influencer le nombre d'accidents dans une région ?"
]

# Styles communs
common_style = {
    'fontSize': 25,
    'margin': '20px',
    'padding': '10px',
    'border': '5px double white',
    'backgroundColor': '#800080',
    'color': 'white',
    'width': '300px',
    'height': '300px',
    'text-align': 'center',
    'verticalAlign': 'middle',
    'textDecoration': 'none',
}

# Définir la mise en page du dashboard
app.layout = html.Div(style={'backgroundColor': '#800000', 'color': 'white', 'height': '100vh'}, children=[
    # Titre de la page de garde
    html.H1("Bienvenue sur notre Dashboard", style={'textAlign': 'center'}),

    # Première ligne de questions
    html.Div([
        dcc.Link(question, href=f'/{visualisation_id}', style=common_style) for visualisation_id, question in zip(list(visualisations.keys())[:4], questions[:4])
    ], style={'display': 'flex', 'justifyContent': 'space-evenly', 'height': '50%'}),

    # Deuxième ligne de questions
    html.Div([
        dcc.Link(question, href=f'/{visualisation_id}', style=common_style) for visualisation_id, question in zip(list(visualisations.keys())[4:], questions[4:])
    ], style={'display': 'flex', 'justifyContent': 'space-evenly', 'height': '50%'}),

    # Contenu de la visualisation
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

    # Noms en haut à droite
    html.Div(
        noms := ["ABARKAN Suhaila, ", "MOUCHRIF Dounia, ", "ROMAN Karina, ", "TISSANDIER Mathilde"],
        style={'position': 'absolute', 'top': '20px', 'right': '20px', 'textAlign': 'center'}
    )
])

# Gérer le changement d'URL pour afficher la bonne visualisation
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname is None or pathname == '/':
        return "Bon retour sur notre dashboard"
    else:
        visualisation_id = pathname.replace('/', '')
        return f"Visualisation sélectionnée : {visualisations.get(visualisation_id, 'Inconnue')}"


if __name__ == '__main__':
    app.run_server(debug=True)
