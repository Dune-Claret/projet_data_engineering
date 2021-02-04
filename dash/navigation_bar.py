# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Couleurs pour la barre de navigation
colors = {
    'theme':'dark',
    'sidebar':'#2b2b2b'
}

# Barre de navigation
navigationBar = dbc.NavbarSimple(
    brand= "TOP ALBUMS IN THE WORLD",
    brand_href="france",
    color=colors['theme'],
    dark=True,
    sticky="top",
    children=[
        dbc.NavItem(dbc.NavLink("France", href="france")),
        dbc.NavItem(dbc.NavLink("USA", href="usa")),
        dbc.NavItem(dbc.NavLink("UK", href="uk")),
    ]
)
