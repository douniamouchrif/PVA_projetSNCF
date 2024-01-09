import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.visualisation import build_boxplot
from data.get_data import get_data_boxplot_t

question = "Le nombre d’incidents varie-t-il drastiquement d’une année à l’autre?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    boxplot_content = build_boxplot(get_data_boxplot_t())
    figure_size = {'width': '100%', 'height': '750px'}
    graph = dcc.Graph(figure=boxplot_content, style=figure_size)
    return [html.Div(children=[
        html.Div([
            dbc.Button("Retour", id="btn-retour1", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'}),
        ]),
        html.Div(graph)
    ]), dcc.Location(id='url-redirect1')]


@callback(
    Output("url-redirect1", "pathname"),
    [Input("btn-retour1", "n_clicks")]
)
def retour_button_callback(n_clicks):
    if n_clicks:
        return '/visualisations'
    raise dash.exceptions.PreventUpdate
