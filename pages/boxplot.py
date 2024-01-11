import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.builder import build_boxplot
from data.get_data import get_data_boxplot_t
from story_telling.box_plot_story import get_text_below_boxplot

question = "Le nombre d’incidents varie-t-il drastiquement d’une année à l’autre?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    boxplot_content = build_boxplot(get_data_boxplot_t())
    figure_size = {'width': '100%', 'height': '750px'}
    graph = dcc.Graph(figure=boxplot_content, style=figure_size)
    avant = dbc.Button(
        "Avant", id="btn-avant2", color="primary", className="mr-1", style={'float': 'left', 'background-color': '#670907'})
    apres = dbc.Button(
        "Après", id="btn-apres2", color="primary", className="mr-1", style={'float': 'right', 'background-color': '#670907'})

    return [html.Div(children=[
        html.Div([
            avant,
            apres,
            dbc.Button("Retour", id="btn-retour2", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'})
        ]),
        html.Div(graph),
        get_text_below_boxplot()
    ]), dcc.Location(id='url-redirect2')]


@callback(
    Output("url-redirect2", "pathname"),
    [Input("btn-retour2", "n_clicks"),
     Input("btn-avant2", "n_clicks"),
     Input("btn-apres2", "n_clicks")]
)
def button_callback(n_clicks_retour, n_clicks_avant, n_clicks_apres):
    if n_clicks_retour:
        return '/visualisations'
    elif n_clicks_avant:
        return '/barplot'
    elif n_clicks_apres:
        return '/incident-map'