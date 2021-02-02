"""
Module pour la page france.
"""

# Imports
import numpy as np
import pandas as pd
import json
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from requests_mongo import get_graphes

# Variable pour la page
country = 'France'
f1, f2, f3 = get_graphes(country)

def generate_dropdown(dataframe, feature):
    dropdown = list()

    for element in dataframe[feature].unique():
        dropdown.append({'label': element, 'value':element})

    return dropdown

# Page pour France
pageFrance = html.Div([

    # Cote gauche
    html.Div(
        [
            # Titre
            html.H4("Top 10"),

            # Break
            html.Br(),
            html.Hr(style={"background-color":"white"}),

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
            html.Hr(style={"background-color":"white"})
        ],
        style = {"flex":1, "padding":"20px"},
    ),

    # Cote droit
    html.Div(
        [
            # Graphique 1
            html.Div([dcc.Graph(figure = f1)], style = {}),

            # Graphique 2
            html.Div([dcc.Graph(figure = f2)], style = {}),

            # Graphique 3
            html.Div([dcc.Graph(figure = f3)], style = {}),
        ],
        style = {"flex":2, "display": "flex", "flex-direction": "column"},
    ),],
    style = {"display":"flex", " padding":"0px", "margin":"0px"}
)