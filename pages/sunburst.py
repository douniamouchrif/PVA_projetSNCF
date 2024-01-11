import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.builder import build_sunburst
from visus.interaction import build_dropdown_year_multi
from data.get_data import get_data_sunburst, get_years_dropdown
from story_telling.sunburst_story import get_text_below_sunburst

question = "Comment le nombre d’incidents par gravité a-t-il évolué ces 8 dernières années ? Quelles sont les principales origines des incidents pour une gravité choisie ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    avant = dbc.Button(
        "Avant", id="btn-avant6", color="primary", className="mr-1", style={'float': 'left', 'background-color': '#670907'})

    return [html.Div(children=[
        html.Div([
            avant,
            dbc.Button("Retour", id="btn-retour6", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'}),
        ]),
        html.Div([
            html.P("Sélectionner une ou plusieurs années à afficher (par défaut toutes les années de 2016 à 2023 sont affichées) :"),
            build_dropdown_year_multi(get_years_dropdown()),
            html.Div(id='sunburst-container', children=[]),
            get_text_below_sunburst(),
        ])
    ]), dcc.Location(id='url-redirect6')]


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
    Output("url-redirect6", "pathname"),
    [Input("btn-retour6", "n_clicks"),
     Input("btn-avant6", "n_clicks")]
)
def button_callback(n_clicks_retour, n_clicks_avant):
    if n_clicks_retour:
        return '/visualisations'
    elif n_clicks_avant:
        return '/scatter'