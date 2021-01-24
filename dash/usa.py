"""
Module pour la page usa.
"""

# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Import local
from requests_mongo import get_graphes

# Variables pour la page
f1, f2, f3 = get_graphes('USA')

# Menu
menu = dbc.Col(
    html.Div([
        dbc.Card(
            [
                # Titre
                html.H4("Top 10"),

                # Liste des options
                html.Ul([
                    # ligne separateur
                    html.Br(),
                    
                    # Titre 2
                    dbc.Button("Album1", id="button-france-album1", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Hr(style={"background-color":"white"}),

                    # Titre 3
                    dbc.Button("Album2", id="button-france-album2", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 4
                    dbc.Button("Album3", id="button-france-album3", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 5
                    dbc.Button("Album4", id="button-france-album4", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 6
                    dbc.Button("Album5", id="button-france-album5", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 7
                    dbc.Button("Album6", id="button-france-album6", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 8
                    dbc.Button("Album7", id="button-france-album7", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 9
                    dbc.Button("Album8", id="button-france-album8", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 10
                    dbc.Button("Album9", id="button-france-album9", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),

                    # Titre 11
                    dbc.Button("Album10", id="button-france-album10", color="light", outline=True, className="mr-1"),

                    # Separation
                    html.Br(),
                    html.Hr(style={"background-color":"white"}),
                ])
            ],
            body=True,
            style={'height':600}
        )
    ]),
    width=4
)

pageUsa = html.Div([
    # Graphique 1
    html.Div([dcc.Graph(id='f1')], style = {}),

    # Graphique 2
    html.Div([dcc.Graph(id='f2')], style = {}),

    # Graphique 3
    html.Div([dcc.Graph(id='f3')], style = {}),
],
style = {"flex":2, "display": "flex", "flex-direction": "column"}
)

