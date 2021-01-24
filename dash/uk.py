"""
Module pour la page uk.
"""

# Import
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats as sc
from requests_mongo import get_graphes

# Variable pour la page
country = 'UK'
f1, f2, f3 = get_graphes(country)

pageUk = html.Div([

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
            html.Hr(style={"background-color":"white"}),  

            # Fenetre pour region specifiee
            dbc.Modal(
                [
                    # Fenetre: Titre
                    dbc.ModalHeader(id="header-france-group"),

                    # Fenetre: Corps
                    dbc.ModalBody([

                        # Gauche: Graphique France homme/femme
                        html.Div([
                            dbc.Card([
                                dbc.CardBody([
                                    dcc.Graph(id="lineplot-france-graph", style={"height":520})
                                ]),

                                dbc.CardFooter([
                                    # Label des annees du slider
                                    #dbc.Label(
                                    #    "From {} to {}:".format(minYear, maxYear),
                                    #    id="label-france-group-graph",
                                    #),

                                    # Selection de l'interval
                                    #dcc.RangeSlider(
                                    #    id="slider-france-group-graph",
                                    #    min=minYear,
                                    #    max=maxYear,
                                    #    value=[minYear, maxYear]
                                    #)
                                ])
                            ], outline=True, color="dark")
                        ], style={"flex":3, "padding-right":5}),

                        # Droite: Graphiques divers
                        html.Div([
                            dbc.Card([

                                # Zone des graphiques
                                dbc.CardBody([
                                    dcc.Graph(id="piechart-france-miscellaneous", style={"height":260, "padding":0}),

                                    html.Div(
                                        html.H1([
                                            dbc.Badge(id="ranking-france-miscellaneous", className="ml-1", color="secondary"),
                                            html.P(id="ranking-text-france-miscellaneous")],
                                        style={"text-align":"center", "padding-top":260* 2/6})
                                    , style={"height":260})
                                ]),

                                # Pied de page des graphiques
                                dbc.CardFooter([
                                    # Label de l'annee selectionnee
                                    #dbc.Label(
                                    #    "During the year {}".format(minYear),
                                    #    id="label-france-miscellaneous"
                                    #),

                                    # Selection de l'annee
                                    #dcc.Slider(
                                    #    id="slider-france-miscellaneous-graph",
                                    #    min=minYear,
                                    #    max=maxYear,
                                    #    value=minYear
                                    #)
                                ]),
                            ], color="dark", outline=True),

                        ], style={"flex":2, "padding-left":5})

                    ], style = {"display":"flex"}),

                    # Fenetre: Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal-france-group", color="danger", outline=True,block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-group",
                size="xl"
            ),
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
