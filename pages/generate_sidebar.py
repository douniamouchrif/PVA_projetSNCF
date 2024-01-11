import dash
from dash import html
import dash_bootstrap_components as dbc

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