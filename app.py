import dash
from dash import html
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#670907",  
}
NAV_LINK_STYLE = {
    "color": "white",
}

PAGE_ORDER = ["Home", "Visualisations", "About us"]


def generate_sidebar(pathname):
    sidebar = html.Div(
        [
            html.Img(src="/static/IMG/logo_sncf.png", id="sidebar-logo",
                     className="animate__animated animate__fadeIn", style={"max-width": "100%", "max-height": "100%"}),
            html.H2("PROJET SNCF", style={"color": "white"}),
            html.Hr(style={"border-color": "white"}),
            html.P("Menu", className="lead", style={"color": "white"}),
            dbc.Nav(
                [
                    dbc.NavLink(
                        f"{page['name']}",
                        href=page["relative_path"],
                        id=f"{page['name'].lower()}-link",
                        style={
                            **NAV_LINK_STYLE,
                            "font-size": "1.5rem" 
                        },
                        active={
                            'font-weight': 'bold'
                        } if page["name"].lower() == pathname.strip('/') else {},
                        className="nav-link-hover", 
                    )
                    for page_name in PAGE_ORDER
                    for page in dash.page_registry.values() if page["name"] == page_name and 'location' in page and page['location'] == 'sidebar'
                ],
                vertical=True,
                pills=True,
                id="sidebar-nav",
            ),
            html.P("ABARKAN Suhaila", style={"color": "white",
                   "font-size": "1.1rem", "margin-top": "100px"}),
            html.P("MOUCHRIF Dounia", style={
                   "color": "white", "font-size": "1.1rem"}),
            html.P("ROMAN Karina", style={
                   "color": "white", "font-size": "1.1rem"}),
            html.P("TISSANDIER Mathilde", style={
                   "color": "white", "font-size": "1.1rem"})
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar


@app.callback(
    [dash.Output(f"{page['name']}-link", "style")
     for page in dash.page_registry.values()],
    [dash.Input("url", "pathname")],
)
def update_navbar_collapse(pathname):
    styles = [{"font-weight": "bold"} if pathname.strip('/') == page_name.lower() else {"font-weight": "normal"}
              for page_name in PAGE_ORDER]
    return styles


app.layout = html.Div(style={'backgroundColor': '#c0c0bb', 'color': 'black', 'min-height': '100vh'}, children=[
    dbc.Row([
        dbc.Col(width=2, children=generate_sidebar("")),
        dbc.Col(width=10, children=dash.page_container)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
