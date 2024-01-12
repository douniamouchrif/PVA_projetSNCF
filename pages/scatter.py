import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from visus.builder import build_scatter
from visus.interaction import build_dropdown_year
from data.get_data import get_data_scatterplot, get_years_dropdown, get_origines_count
from story_telling.scatter_plot_story import get_text_below_scatter

question = "Comment les gravités des causes d’incidents ont-elles évolué au cours de ces 8 dernières années ? Et combien y-a-t-il d'incidents par mois ?"

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def layout():
    dropdown = build_dropdown_year(get_years_dropdown())
    graph = dcc.Graph(id='scatterplot')
    incident_origines = html.Div(id='incident_origines')
    avant = dbc.Button(
        "Avant", id="btn-avant5", color="primary", className="mr-1", style={'float': 'left', 'background-color': '#670907'})
    apres = dbc.Button(
        "Après", id="btn-apres5", color="primary", className="mr-1", style={'float': 'right', 'background-color': '#670907'})

    return [html.Div(children=[
        html.Div([
            avant,
            apres,
            dbc.Button("Retour", id="btn-retour5", color="primary",
                       className="mr-1", style={'float': 'right', 'background-color': '#670907'}),
            html.H3(question, style={'textAlign': 'center'})
        ]),
        html.Div([html.P("Sélectionner une année :"),
                  dropdown,
                  graph,
                  incident_origines,
                  get_text_below_scatter()
                  ])
    ]), dcc.Location(id='url-redirect5')]


@callback(
    Output('scatterplot', 'figure'),
    Output('incident_origines', 'children'),
    [Input('dropdown', 'value'),
     Input('scatterplot', 'selectedData')]
)
def graph_update(dropdown_values, selected_data):
    if dropdown_values is None:
        dropdown_values = get_years_dropdown()[0]
    data = get_data_scatterplot(dropdown_values)
    figure = build_scatter(data, dropdown_values)

    origines_count = {}
    year = None
    month = None
    if selected_data and 'points' in selected_data:
        selected_points = selected_data['points']
        if selected_points:
            full_date = selected_points[0]['x']
            year, month = full_date.split('-')[:2]
            origines_count = get_origines_count(year, month)
    origines_list = [html.Li(f"Mois sélectionné : {month}")] + [html.Li(f"Année sélectionnnée : {year}")] + [html.Br()] + [html.Li(f"{origine}: {count}")
                                                                                                                           for origine, count in origines_count.items()]
    return figure, html.Ul(origines_list)


@callback(
    Output("url-redirect5", "pathname"),
    [Input("btn-retour5", "n_clicks"),
     Input("btn-avant5", "n_clicks"),
     Input("btn-apres5", "n_clicks")]
)
def button_callback(n_clicks_retour, n_clicks_avant, n_clicks_apres):
    if n_clicks_retour:
        return '/visualisations'
    elif n_clicks_avant:
        return '/lineplot-heapmap'
    elif n_clicks_apres:
        return '/sunburst'
