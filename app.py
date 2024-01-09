import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True, assets_folder='assets_folder')

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#670907",  # Couleur de fond de la sidebar
}
NAV_LINK_STYLE = {
    "color": "white",
}

# Define the order of pages
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
                            "font-size": "1.5rem"  # Set the font size here
                        },
                        active={
                            'font-weight': 'bold'
                        } if page["name"].lower() == pathname.strip('/') else {},
                        className="nav-link-hover",  # Ajoutez la nouvelle classe CSS pour le survol
                    )
                    for page_name in PAGE_ORDER
                    for page in dash.page_registry.values() if page["name"] == page_name and 'location' in page and page['location'] == 'sidebar'
                ],
                vertical=True,
                pills=True,
                id="sidebar-nav",
            ),
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


"""import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

external_stylesheets = ['styles.css']

# ...

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets], suppress_callback_exceptions=True)

# Fonction pour générer la sidebar
def generate_sidebar():
    sidebar_items = [
        dbc.NavLink(f"{page['name']}",
                    href=page["relative_path"], id=f"{page['name']}-link")
        for page in dash.page_registry.values() if 'location' in page and page['location'] == 'sidebar'
    ]

    # Ajoutez le contenu de votre barre latérale ici
    sidebar_content = html.Div([
        html.Div([
            html.Span([
                html.I(className='bx bx-chevron-left'),
                html.Img(src="./img/logo.png", className="logo", alt=""),
                html.H3("Aqumex", className="hide")
            ], className="sidebar-top"),
            html.Div([
                html.I(className='bx bx-search'),
                dcc.Input(type="text", className="hide", placeholder="Quick Search ...")
            ], className="search"),
            html.Div([
                html.Ul([
                    html.Div(className="active-tab"),
                    html.Li([
                        html.A([
                            html.Div([
                                html.I(className='bx bx-tachometer'),
                                html.I(className='bx bxs-tachometer')
                            ], className='icon'),
                            html.Span("Dashboard", className="link hide")
                        ], href="#", className="active")
                    ], className="tooltip-element"),
                    # Ajoutez d'autres liens de la barre latérale ici
                ]),
                html.Div([
                    html.Span("Dashboard"),
                    html.Span("Projects"),
                    html.Span("Messages"),
                    html.Span("Analytics")
                ], className="tooltip")
            ], className="sidebar-links"),
            html.H4("Shortcuts", className="hide"),
            html.Ul([
                html.Li([
                    html.A([
                        html.Div([
                            html.I(className='bx bx-notepad'),
                            html.I(className='bx bxs-notepad')
                        ], className='icon'),
                        html.Span("Tasks", className="link hide")
                    ], href="#")
                ], className="tooltip-element"),
                # Ajoutez d'autres liens de la barre latérale ici
            ]),
            html.Div([
                html.Span("Tasks"),
                html.Span("Help"),
                html.Span("Settings")
            ], className="tooltip")
        ], className="sidebar-links"),
        html.Div([
            html.A([
                html.I(className='bx bx-user')
            ], href="#", className="account tooltip-element"),
            html.Div([
                html.Div([
                    html.Img(src="./img/face-1.png", alt=""),
                    html.Div([
                        html.H3("John Doe"),
                        html.H5("Admin")
                    ], className="admin-info")
                ], className="admin-profile hide"),
                html.A([
                    html.I(className='bx bx-log-out')
                ], href="#", className="log-out")
            ], className="admin-user tooltip-element"),
            html.Div([
                html.Span("John Doe"),
                html.Span("Logout")
            ], className="tooltip")
        ], className="sidebar-footer")
    ], className="sidebar-content")

    return dbc.Nav(sidebar_items + [sidebar_content], vertical=True, pills=True)

# Mise en page principale
app.layout = html.Div(style={'backgroundColor': 'var(--main-color)', 'color': '#fff', 'min-height': '100vh'}, children=[
    dbc.Row([
        dbc.Col(width=2, children=generate_sidebar()),
        dbc.Col(width=10, children=dash.page_container)
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)"""


'''import dash
from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

external_scripts = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# Ajoutez ces lignes pour personnaliser le style de survol
external_scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css"]

app = Dash(__name__, use_pages=True, external_stylesheets=[
           dbc.themes.BOOTSTRAP], external_scripts=external_scripts, suppress_callback_exceptions=True)

app.clientside_callback(
    """
    function(hovered) {
        if (hovered) {
            document.getElementById('sidebar-title').style.color = 'red';  // Changez la couleur selon vos préférences
        } else {
            document.getElementById('sidebar-title').style.color = '';  // Réinitialisez la couleur lorsque la souris n'est pas dessus
        }
    }
    """,
    Output('sidebar-title', 'style'),
    [Input('sidebar-title', 'n_clicks')],
    prevent_initial_call=True
)

# Fonction pour générer la sidebar


def generate_sidebar():
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    }
    sidebar = html.Div(
        [
            html.H1("SNCF #mettre un logo",
                    className="display-4 animate__animated animate__fadeIn", id="sidebar-title"),
            html.H2("ABARKAN & MOUCHRIF"),
            html.Hr(),
            html.P(
                "Menu", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink(f"{page['name']}",
                                href=page["relative_path"], id=f"{page['name']}-link")
                    for page in dash.page_registry.values() if 'location' in page and page['location'] == 'sidebar'
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )
    return dbc.Nav(sidebar, vertical=True, pills=True)


# Mise en page principale
app.layout = html.Div(style={'backgroundColor': '#001F3F', 'color': 'black', 'min-height': '100vh'}, children=[
    dbc.Row([
        dbc.Col(width=2, children=generate_sidebar()),
        dbc.Col(width=10, children=dash.page_container)
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)'''


"""dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("About", href="/about")),
        ],
        brand="ABARKAN Suhaila, MOUCHRIF Dounia, ROMAN Karina & TISSANDIER Mathilde",
        color="primary",
        dark=True,
    ),"""
