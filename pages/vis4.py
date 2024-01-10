import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.visualisation import build_sunburst
from visus.interaction import build_dropdown_year_multi
from data.get_data import get_data_sunburst, get_years_dropdown

question = "Comment le nombre d’incidents par gravité a-t-il évolué ces 8 dernières années ? Quelles sont les principales origines des incidents pour une gravité choisie ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    return [html.Div(children=[
        html.Div([
            dbc.Button("Retour", id="btn-retour4", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'}),
        ]),
        html.Div([
            html.P("Sélectionner une ou plusieurs années à afficher (par défaut toutes les années de 2016 à 2023 sont affichées) :"),
            build_dropdown_year_multi(get_years_dropdown()),
            html.Div(id='sunburst-container', children=[]),
            html.P("Rappelons que les niveaux de gravité des incidents vont de 1 (le moins grave) à 6 (le plus grave)."),
            html.P("Ces sunburst représentent la répartition des incidents en fonction des gravités, puis lorsque nous cliquons sur une gravité, nous obtenons la répartition des incidents en fonction des causes pour la gravité séléctonnée. Grâce au dropdown nous avons la possibilité de séléctionner seulement les années qui nous intéressent, par défaut, au début toutes les années sont séléctonnées."),
            html.P("En parcourant les sunbursts, nous avons pu nous rendre compte que les causes les plus réccurentes des incidents sont Réseau, Mobilité et Voyageur avec des gravités plus ou moins élevées, pouvant aller d'un petit excès de vitesse à un défaut de signalisation, un déraillement ou encore un accident de personne. Notons que dans le temps, les incidents de causes Réseau ont une légère tendence à être plus nombreux et aussi, la cause Voyageur occupe une place plus importante à partir de 2020 (l'année de la crise du covid-19, ce qui pourrait être une explication)."),
            html.P("Parmis toutes les années, les incidents de niveau de gravité 1 et 2 sont très peu nombreux, voir inexistants pour la plupart des années. Les incidents associés à de tels gravités n'engagent pas la sécurité des passagers à l'intérieur ou extérieur du train."),
            html.P("Ensuite, nous avons aussi pu remarquer à travers ces sunbursts que les incidents de gravités 4 sont majoritaires pour chaque année. Les causes principales associées à cette gravité sont les causes Réseau et Mobilité ainsi que Voyageur à partir de 2020."),
            html.P("Enfin, l'année 2023 peut être considérée comme la plus dangereuse avec tous ces incidents (au nombre de 237) de gravité 4 minimum. Nous observons une forte augmentation des incidents de gravité 5. Les causes principales associées à la gravité 5 sont Accidents de personnes et Collision passage à niveau, qui sont des événements plutôt graves ce qui exlique un tel niveau de gravité."),
            
        ])
    ]), dcc.Location(id='url-redirect4')]


@callback(Output(component_id='sunburst-container', component_property='children'),
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


@callback(
    Output("url-redirect4", "pathname"),
    [Input("btn-retour4", "n_clicks")]
)
def retour_button_callback(n_clicks):
    if n_clicks:
        return '/visualisations'
    raise dash.exceptions.PreventUpdate
