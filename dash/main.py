# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
import pymongo
from pymongo import MongoClient

# Imports de fichiers en local
from uk import (pageUk, tab_1_uk, tab_2_uk)
from usa import (pageUsa, tab_1_usa, tab_2_usa)
from navigation_bar import navigationBar
from france import (pageFrance, tab_1_france, tab_2_france)

# Application: Dashboard
if __name__ == '__main__':

    # Creer une application Dash
    app = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.DARKLY],
        suppress_callback_exceptions=True
    )

    # Corps de l'application
    app.layout = html.Div([
        navigationBar,
        dcc.Location(id='url', refresh=False),
        html.Div(id='page')
    ])

    # Interactivite: Navigation de page
    @app.callback(
        dash.dependencies.Output('page', 'children'),
        [dash.dependencies.Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/france':
            return pageFrance
        elif pathname == '/usa':
            return pageUsa 
        elif pathname == '/uk':
            return pageUk    
        else:
            return pageFrance

    # Interactivite : Ouverture d'une fenêtre
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    # USA - Interactivite : Ouverture d'une fenêtre
    app.callback(
        dash.dependencies.Output("modal-usa-album-1", "is_open"),
        [dash.dependencies.Input("button-usa-album1", "n_clicks"), dash.dependencies.Input("close-usa-album-1", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-1", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-2", "is_open"),
        [dash.dependencies.Input("button-usa-album2", "n_clicks"), dash.dependencies.Input("close-usa-album-2", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-2", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-3", "is_open"),
        [dash.dependencies.Input("button-usa-album3", "n_clicks"), dash.dependencies.Input("close-usa-album-3", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-3", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-4", "is_open"),
        [dash.dependencies.Input("button-usa-album4", "n_clicks"), dash.dependencies.Input("close-usa-album-4", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-4", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-5", "is_open"),
        [dash.dependencies.Input("button-usa-album5", "n_clicks"), dash.dependencies.Input("close-usa-album-5", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-5", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-6", "is_open"),
        [dash.dependencies.Input("button-usa-album6", "n_clicks"), dash.dependencies.Input("close-usa-album-6", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-6", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-7", "is_open"),
        [dash.dependencies.Input("button-usa-album7", "n_clicks"), dash.dependencies.Input("close-usa-album-7", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-7", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-8", "is_open"),
        [dash.dependencies.Input("button-usa-album8", "n_clicks"), dash.dependencies.Input("close-usa-album-8", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-8", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-9", "is_open"),
        [dash.dependencies.Input("button-usa-album9", "n_clicks"), dash.dependencies.Input("close-usa-album-9", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-9", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-usa-album-10", "is_open"),
        [dash.dependencies.Input("button-usa-album10", "n_clicks"), dash.dependencies.Input("close-usa-album-10", "n_clicks")],
        [dash.dependencies.State("modal-usa-album-10", "is_open")],
    )(toggle_modal)

    # UK - Interactivite : Ouverture d'une fenêtre
    app.callback(
        dash.dependencies.Output("modal-uk-album-1", "is_open"),
        [dash.dependencies.Input("button-uk-album1", "n_clicks"), dash.dependencies.Input("close-uk-album-1", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-1", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-2", "is_open"),
        [dash.dependencies.Input("button-uk-album2", "n_clicks"), dash.dependencies.Input("close-uk-album-2", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-2", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-3", "is_open"),
        [dash.dependencies.Input("button-uk-album3", "n_clicks"), dash.dependencies.Input("close-uk-album-3", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-3", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-4", "is_open"),
        [dash.dependencies.Input("button-uk-album4", "n_clicks"), dash.dependencies.Input("close-uk-album-4", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-4", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-5", "is_open"),
        [dash.dependencies.Input("button-uk-album5", "n_clicks"), dash.dependencies.Input("close-uk-album-5", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-5", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-6", "is_open"),
        [dash.dependencies.Input("button-uk-album6", "n_clicks"), dash.dependencies.Input("close-uk-album-6", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-6", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-7", "is_open"),
        [dash.dependencies.Input("button-uk-album7", "n_clicks"), dash.dependencies.Input("close-uk-album-7", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-7", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-8", "is_open"),
        [dash.dependencies.Input("button-uk-album8", "n_clicks"), dash.dependencies.Input("close-uk-album-8", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-8", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-9", "is_open"),
        [dash.dependencies.Input("button-uk-album9", "n_clicks"), dash.dependencies.Input("close-uk-album-9", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-9", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-uk-album-10", "is_open"),
        [dash.dependencies.Input("button-uk-album10", "n_clicks"), dash.dependencies.Input("close-uk-album-10", "n_clicks")],
        [dash.dependencies.State("modal-uk-album-10", "is_open")],
    )(toggle_modal)

    # FRANCE - Interactivite : Ouverture d'une fenêtre
    app.callback(
        dash.dependencies.Output("modal-france-album-1", "is_open"),
        [dash.dependencies.Input("button-france-album1", "n_clicks"), dash.dependencies.Input("close-france-album-1", "n_clicks")],
        [dash.dependencies.State("modal-france-album-1", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-2", "is_open"),
        [dash.dependencies.Input("button-france-album2", "n_clicks"), dash.dependencies.Input("close-france-album-2", "n_clicks")],
        [dash.dependencies.State("modal-france-album-2", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-3", "is_open"),
        [dash.dependencies.Input("button-france-album3", "n_clicks"), dash.dependencies.Input("close-france-album-3", "n_clicks")],
        [dash.dependencies.State("modal-france-album-3", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-4", "is_open"),
        [dash.dependencies.Input("button-france-album4", "n_clicks"), dash.dependencies.Input("close-france-album-4", "n_clicks")],
        [dash.dependencies.State("modal-france-album-4", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-5", "is_open"),
        [dash.dependencies.Input("button-france-album5", "n_clicks"), dash.dependencies.Input("close-france-album-5", "n_clicks")],
        [dash.dependencies.State("modal-france-album-5", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-6", "is_open"),
        [dash.dependencies.Input("button-france-album6", "n_clicks"), dash.dependencies.Input("close-france-album-6", "n_clicks")],
        [dash.dependencies.State("modal-france-album-6", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-7", "is_open"),
        [dash.dependencies.Input("button-france-album7", "n_clicks"), dash.dependencies.Input("close-france-album-7", "n_clicks")],
        [dash.dependencies.State("modal-france-album-7", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-8", "is_open"),
        [dash.dependencies.Input("button-france-album8", "n_clicks"), dash.dependencies.Input("close-france-album-8", "n_clicks")],
        [dash.dependencies.State("modal-france-album-8", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-9", "is_open"),
        [dash.dependencies.Input("button-france-album9", "n_clicks"), dash.dependencies.Input("close-france-album-9", "n_clicks")],
        [dash.dependencies.State("modal-france-album-9", "is_open")],
    )(toggle_modal)

    app.callback(
        dash.dependencies.Output("modal-france-album-10", "is_open"),
        [dash.dependencies.Input("button-france-album10", "n_clicks"), dash.dependencies.Input("close-france-album-10", "n_clicks")],
        [dash.dependencies.State("modal-france-album-10", "is_open")],
    )(toggle_modal)

    # USA - Interactivité : Construction des onglets principaux 

    @app.callback(
        Output('tabs-content-inline-usa', 'children'), 
        Input('tabs-styled-with-inline-usa', 'value')
    )
    def render_content_usa(tab):
        if tab == 'tab-1-usa':
            return tab_1_usa
        elif tab == 'tab-2-usa':
            return tab_2_usa

    # UK - Interactivité : Construction des onglets principaux 

    @app.callback(
        Output('tabs-content-inline-uk', 'children'), 
        Input('tabs-styled-with-inline-uk', 'value')
    )
    def render_content_uk(tab):
        if tab == 'tab-1-uk':
            return tab_1_uk
        elif tab == 'tab-2-uk':
            return tab_2_uk

    # FRANCE - Interactivité : Construction des onglets principaux 

    @app.callback(
        Output('tabs-content-inline-france', 'children'), 
        Input('tabs-styled-with-inline-france', 'value')
    )
    def render_content_france(tab):
        if tab == 'tab-1-france':
            return tab_1_france
        elif tab == 'tab-2-france':
            return tab_2_france

    # Titre de l'application
    app.title = "World's top albums"

    # Execute l'application Dash sur un serveur web local
    app.run_server(debug=False)

    pass