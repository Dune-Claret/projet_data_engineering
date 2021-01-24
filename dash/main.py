# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Imports de fichiers en local
from uk import pageUk
from usa import pageUsa
from navigation_bar import navigationBar
from france import pageFrance

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

    # FRANCE - Interactivite: Ouverture fenetre pour region specifique
    @app.callback(
        [dash.dependencies.Output("modal-france-group", "is_open"),
        dash.dependencies.Output("header-france-group", "children")],
        [dash.dependencies.Input("button-france-group", "n_clicks"),
        dash.dependencies.Input("close-modal-france-group", "n_clicks"),
        dash.dependencies.Input("dropdown-france-group-location", "value")],
        [dash.dependencies.State("modal-france-group", "is_open")]
    )
    def open_modal(n1, n2, location, is_open):
        if n1 or n2:
            return not is_open, location

        return is_open, None

    # FRANCE - Interactivite: Ouverture fenetre pour region specifique bis
    @app.callback(
        dash.dependencies.Output("button-france-group", "n_clicks"),
        dash.dependencies.Input("close-modal-france-group", "n_clicks"),
    )
    def reset_button_submit(n_clicks_close):
        return None

    # Titre de l'application
    app.title = "World's top albums"

    # Execute l'application Dash sur un serveur web local
    app.run_server(debug=False)

    pass

