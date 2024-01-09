import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.visualisation import build_lineplot, build_heapmap
from visus.interaction import build_radioitems
from data.get_data import get_data_lineplot

question = "Comment le nombre d’incidents par gravité a-t-il évolué ces 8 dernières années ? Quelles sont les principales origines des incidents pour une gravité choisie ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    lineplot = dcc.Graph(id='incident-graph'),
    heapmap = dcc.Graph(id='heatmap')
    return [html.Div(children=[
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
    [Input("btn-retour3", "n_clicks")]
)
def retour_button_callback(n_clicks):
    if n_clicks:
        return '/visualisations'
    raise dash.exceptions.PreventUpdate
