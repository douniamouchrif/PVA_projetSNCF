import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.visualisation import barplot_1522
from visus.interaction import build_range_slider
from data.get_data import get_data_barplot_1522, get_years_range_slider

question = "Est-ce que les régions les plus fréquentées sont celles où se produisent le plus d’incidents ? Pour chaque région, quelle est la cause d’incidents qui atteint le plus grand niveau de gravité ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    rangeslider = build_range_slider(*get_years_range_slider())
    graph = dcc.Graph(id='barplot')
    return [html.Div(children=[
        html.Div([
            dbc.Button("Retour", id="btn-retour5", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'}),
        ]),
        html.Div([html.P("Sélectionner un interval d'années :"),
                  rangeslider,
                  graph
                  ])
    ]), dcc.Location(id='url-redirect5')]


@callback(Output(component_id='barplot', component_property='figure'),
          [Input(component_id='rangeslider', component_property='value')])
def graph_update(rangeslider_value):
    if rangeslider_value is None:
        rangeslider_value = get_years_range_slider()  # Valeurs par défaut du slider
    data = get_data_barplot_1522(rangeslider_value)
    return barplot_1522(data)


@callback(
    Output("url-redirect5", "pathname"),
    [Input("btn-retour5", "n_clicks")]
)
def retour_button_callback(n_clicks):
    if n_clicks:
        return '/visualisations'
    raise dash.exceptions.PreventUpdate
