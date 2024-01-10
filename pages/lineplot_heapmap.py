import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.visualisation import build_lineplot, build_heapmap
from visus.interaction import build_radioitems
from data.get_data import get_data_lineplot

question = "Quelles sont les causes des accidents les plus récurrentes ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    lineplot = dcc.Graph(id='incident-graph'),
    heapmap = dcc.Graph(id='heatmap')
    avant = dbc.Button(
        "Avant", id="btn-avant3", color="primary", className="mr-1", style={'float': 'left', 'background-color': '#670907'})
    apres = dbc.Button(
        "Après", id="btn-apres3", color="primary", className="mr-1", style={'float': 'right', 'background-color': '#670907'})

    return [html.Div(children=[
        avant,
        apres,
        dbc.Button("Retour", id="btn-retour3", color="primary",
                   className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
        html.H3(question, style={'textAlign': 'center'}),
        build_radioitems(),
        html.Div(lineplot),
        html.Div(heapmap),
        dcc.Location(id='url-redirect3')
    ])]


@callback(
    [Output('incident-graph', 'figure'),
     Output('heatmap', 'figure')],
    [Input('origine-radio', 'value'),
     Input('incident-graph', 'clickData'),
     Input('cumulative-radio', 'value')]
)
def update_graph(selected_option, click_data, cumulative_mode):
    df = get_data_lineplot()

    fig_line = build_lineplot(df, selected_option, cumulative_mode)
    fig_heatmap = build_heapmap(df, selected_option, click_data)
    return fig_line, fig_heatmap


@callback(
    Output("url-redirect3", "pathname"),
    [Input("btn-retour3", "n_clicks"),
     Input("btn-avant3", "n_clicks"),
     Input("btn-apres3", "n_clicks")]
)
def button_callback(n_clicks_retour, n_clicks_avant, n_clicks_apres):
    if n_clicks_retour:
        return '/visualisations'
    elif n_clicks_avant:
        return '/boxplot'
    elif n_clicks_apres:
        return '/scatter'
