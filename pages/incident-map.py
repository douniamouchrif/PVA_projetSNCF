import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.builder import build_map, fetch_and_process_lines
from visus.interaction import build_radioitems_map, generate_button_div
from data.get_data import get_data_lines, get_data_regions, get_min_max_df, lineE_T
from story_telling.barplot_story import get_text_below_barplot

question = "Quelles sont les regions les plus impactées par les incidents ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    incident_map = dcc.Graph(id='incident-map')
    avant = dbc.Button(
        "Avant", id="btn-avant3", color="primary", className="mr-1", style={'float': 'left', 'background-color': '#670907'})
    apres = dbc.Button(
        "Après", id="btn-apres3", color="primary", className="mr-1", style={'float': 'right', 'background-color': '#670907'})
    start_date, end_date = get_min_max_df(get_data_lines())
    start_date_str = str(start_date)
    end_date_str = str(end_date)
    datepickerrange, radioitems = build_radioitems_map(start_date_str, end_date_str)
    button_div = generate_button_div()

    return html.Div(children=[
        avant,
        apres,
        dbc.Button("Retour", id="btn-retour3", color="primary",
                   className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
        html.H3(question, style={'textAlign': 'center'}),
        datepickerrange,
        radioitems,
        button_div,
        html.Div(incident_map),
        get_text_below_barplot(),
        dcc.Location(id='url-redirect3')
    ])

lines_layer = None

@callback(
    Output('incident-map', 'figure'),
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('map-display-option', 'value'),
     Input('button-no-electric-lines', 'n_clicks'),
     Input('button-with-electric-lines', 'n_clicks'),
     Input('button-with-lines-types', 'n_clicks')]
)
def update_map_and_redirect(start_date, end_date, display_option, n_clicks_no_lines, n_clicks_with_lines, n_clicks_with_lines_types):
    global lines_layer
    df_combined = get_data_lines()
    regions = get_data_regions()
    data_lines = lineE_T()

    fig_fetch_and_process_lines = fetch_and_process_lines(data_lines)
    fig_map = build_map(lines_layer, start_date, end_date, fig_fetch_and_process_lines, regions, df_combined, display_option,
                        n_clicks_no_lines, n_clicks_with_lines, n_clicks_with_lines_types)
    return fig_map

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
        return '/lineplot-heapmap'