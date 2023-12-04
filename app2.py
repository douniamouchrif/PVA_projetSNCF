from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from visus.barplot import barplot_1522, build_range_slider
from visus.scatterplot import build_scatter23, build_scatter1522
from visus.bam import build_boxplot
from visus.lineplot import build_lineplot
from visus.sunburst import build_sunburst, build_dropdown_year, build_dropdown_year_multi 
from data.get_data import get_data_boxplot, get_data_sunburst, get_data_scatterplot23, get_data_scatterplot1522, get_years, get_data_barplot_1522, get_data_lineplot, get_year_barplot

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

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

app.layout = html.Div(style={'backgroundColor': '#001F3F', 'color': 'white', 'min-height': '100vh'}, children=[
    # Navbar
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("About", href="/about")),
        ],
        color="primary",
        dark=True,
    ),
    
    # Contenu de la visualisation et autres éléments
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    # Fenêtre modale "Coming Soon"
    dbc.Modal(
        [
            dbc.ModalHeader("Coming Soon"),
            dbc.ModalBody(
                "La visualisation sélectionnée sera bientôt disponible."),
            dbc.ModalFooter(
                dbc.Button("Fermer", id="close-modal", className="ml-auto")
            ),
        ],
        id="coming-soon-modal",
        centered=True,
        is_open=False  # Initialisation à fermé
    )
])

home_layout = html.Div(style={'backgroundColor': '#001F3F', 'color': 'white', 'height': '100vh'}, children=[

    html.H1("Bienvenue sur notre Dashboard", style={'textAlign': 'center'}),

    html.Div([
        dcc.Link(question, href=f'/{visualisation_id}', style={'fontSize': min(25, max(15, 400 // len(question))), 'margin': '20px', 'padding': '10px', 'border': '5px double white', 'backgroundColor': '#003366', 'color': 'white', 'width': '300px', 'height': '300px', 'text-align': 'center', 'verticalAlign': 'middle', 'textDecoration': 'none'}) for visualisation_id, question in zip(list(visualisations.keys())[:4], questions[:4])
    ], style={'display': 'flex', 'justifyContent': 'space-evenly', 'height': '50%'}),

    html.Div([
        dcc.Link(question, href=f'/{visualisation_id}', style={'fontSize': min(25, max(15, 400 // len(question))), 'margin': '20px', 'padding': '10px', 'border': '5px double white', 'backgroundColor': '#003366', 'color': 'white', 'width': '300px', 'height': '300px', 'text-align': 'center', 'verticalAlign': 'middle', 'textDecoration': 'none'}) for visualisation_id, question in zip(list(visualisations.keys())[4:], questions[4:])
    ], style={'display': 'flex', 'justifyContent': 'space-evenly', 'height': '50%'}),
    html.Div(
        noms := ["ABARKAN Suhaila, ", "MOUCHRIF Dounia, ", "ROMAN Karina, ", "TISSANDIER Mathilde"],
        style={'position': 'absolute', 'top': '20px',
               'left': '5px', 'textAlign': 'center'}
    )
])

@app.callback([Output('page-content', 'children'), Output("coming-soon-modal", "is_open")],
              [Input('url', 'pathname'), Input("close-modal", "n_clicks")],
              [State("coming-soon-modal", "is_open")])
def display_page_and_modal(pathname, n, is_open):
    if pathname is None or pathname == '/':
        return home_layout, is_open
    elif pathname == '/about':
        return (
            html.Div([
                html.H1("About Page", style={'textAlign': 'center'}),
            ]),
            is_open)
    elif pathname == '/vis1': 
        boxplot_content = build_boxplot(get_data_boxplot())
        figure_size = {'width': '100%', 'height': '750px'}
        graph = dcc.Graph(figure=boxplot_content, style = figure_size)
        return [html.Div(children=[
                    html.H3(questions[0],
                            style={'textAlign': 'center'}),
                    html.Div(graph)]), is_open]
    elif pathname == '/vis2':  
        dropdown = build_dropdown_year(get_years())
        graph = dcc.Graph(id='scatterplot')
        return [html.Div(children=[
                html.H3(questions[1],
                        style={'textAlign': 'center'}),
                html.Div([html.P("Sélectionner une année (par la suite on rajoutera la possiblité d'en séléctionner plusieurs) :"),
                          dropdown,
                          graph
                          ])]), is_open]
    elif pathname == '/vis3':
        lineplot_content = build_lineplot(get_data_lineplot())
        graph = dcc.Graph(figure=lineplot_content)
        return [html.Div(children=[
                html.H3(questions[2],
                        style={'textAlign': 'center'}),
                html.Div(graph)]), is_open]
    elif pathname == '/vis4':  
        return [html.Div(children=[
                html.H3(questions[3], style={'textAlign': 'center'}),
                html.Div([html.P("Sélectionner une ou plusieurs années à afficher (par défaut toutes les années de 2016 à 2022 sont affichées) :"),
                build_dropdown_year_multi(get_years()),
                html.Div(id='sunburst-container', children=[])])]), is_open]
    elif pathname == '/vis5': 
        rangeslider = build_range_slider(*get_year_barplot())
        graph = dcc.Graph(id='barplot')
        return [html.Div(children=[
                html.H3(questions[4],
                        style={'textAlign': 'center'}),
                html.Div([html.P("Sélectionner un interval d'années :"),
                          rangeslider,
                          graph
                          ])]), is_open]
    else:
        visualisation_id = pathname.replace('/', '')
        if visualisation_id in visualisations:
            return f"Visualisation sélectionnée : {visualisations[visualisation_id]}", not is_open
        else:
            return "Inconnue", not is_open

# Scatterplot
@app.callback(Output(component_id='scatterplot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_values):
    if dropdown_values is None:
        dropdown_values = get_years()[0]
    dataa = None
    if dropdown_values == '2023':
        dataa = get_data_scatterplot23()
        return build_scatter23(dataa)
    else:
        dataa = get_data_scatterplot1522(dropdown_values)
        return build_scatter1522(dataa)

# Sunburst
@app.callback(Output(component_id='sunburst-container', component_property='children'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_values):
    if dropdown_values is None or len(dropdown_values) == 0:
        return html.Div(children=[
            html.H1("Veuillez selectionner au moins une année")])
    graphs = []
    for year in dropdown_values:
        data = get_data_sunburst(year)
        fig = build_sunburst(data)
        graph = dcc.Graph(figure=fig)
        graph_with_title = html.Div([
            html.H3(f"Année {year}", style={'textAlign': 'center'}),
            graph
        ], style={'width': '30%', 'display': 'inline-block', 'margin': '1%', 'verticalAlign': 'top'})
        graphs.append(graph_with_title)
    return graphs

# Barplot
@app.callback(Output(component_id='barplot', component_property='figure'),
              [Input(component_id='rangeslider', component_property='value')])
def graph_update(rangeslider_value):
    if rangeslider_value is None:
        rangeslider_value = get_year_barplot()  # Valeurs par défaut du slider
    data = get_data_barplot_1522(rangeslider_value)
    return barplot_1522(data)

if __name__ == '__main__':
    app.run_server(debug=True)
