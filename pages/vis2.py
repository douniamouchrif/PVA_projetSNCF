import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.visualisation import build_scatter
from visus.interaction import build_dropdown_year
from data.get_data import get_data_scatterplot, get_years_dropdown

question = "Comment les causes d’incidents ont-elles évolué au cours de ces 8 dernières années?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    dropdown = build_dropdown_year(get_years_dropdown())
    graph = dcc.Graph(id='scatterplot')
    return [html.Div(children=[
        html.Div([
            dbc.Button("Retour", id="btn-retour2", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'}),
        ]),
        html.Div([html.P("Sélectionner une année :"),
                  dropdown,
                  graph
                  ])
    ]), dcc.Location(id='url-redirect2')]


@callback(Output(component_id='scatterplot', component_property='figure'),
          [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_values):
    if dropdown_values is None:
        dropdown_values = get_years_dropdown()[0]
    data = get_data_scatterplot(dropdown_values)
    return build_scatter(data, dropdown_values)


@callback(
    Output("url-redirect2", "pathname"),
    [Input("btn-retour2", "n_clicks")]
)
def retour_button_callback(n_clicks):
    if n_clicks:
        return '/visualisations'
    raise dash.exceptions.PreventUpdate
