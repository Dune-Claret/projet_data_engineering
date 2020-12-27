# Import
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
    brand= "Dashboard",
    brand_href="page2",
    color=colors['theme'],
    dark=True,
    sticky="top",
    children=[
        dbc.NavItem(dbc.NavLink("Page2", href="page2")),
        dbc.NavItem(dbc.NavLink("Page1", href="page1")),
        dbc.NavItem(dbc.NavLink("Analytics", href="analytics")),
    ]
)
