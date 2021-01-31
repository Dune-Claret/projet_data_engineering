"""
Module pour la page France.
"""

# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats as sc

# Import local
#from requests_mongo import get_graphes

# Variables pour la page
country = 'France'
#f1, f2, f3 = get_graphes(country)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'color': 'black',
    'padding': '6px'
}

pageFrance = html.Div([
    # Construction des onglets principaux
    dcc.Tabs(id="tabs-styled-with-inline-france", value='tab-1-france', children=[
        # Premier onglet "Top 10 best-selling albums"
        dcc.Tab(label='Top 10 best-selling albums', value='tab-1-france', style=tab_style, selected_style=tab_selected_style),
        # Second onglet "Graphs and statistics"
        dcc.Tab(label='Graphs and statistics', value='tab-2-france', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline-france')
])

tab_1_france = html.Div([
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

            # Fenêtre 1
            dbc.Modal(
                [
                    # Fenêtre 1 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 1 : Corps
                    dbc.ModalBody("Information on the album1."),
                    
                    # Fenêtre 1 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-1", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-1",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Hr(style={"background-color":"white"}),

            # Titre 3
            dbc.Button("Album2", id="button-france-album2", color="light", outline=True, className="mr-1"),

            # Fenêtre 2
            dbc.Modal(
                [
                    # Fenêtre 2 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 2 : Corps
                    dbc.ModalBody("Information on the album2."),
                    
                    # Fenêtre 2 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-2", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-2",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 4
            dbc.Button("Album3", id="button-france-album3", color="light", outline=True, className="mr-1"),

            # Fenêtre 3
            dbc.Modal(
                [
                    # Fenêtre 3 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 3 : Corps
                    dbc.ModalBody("Information on the album3."),
                    
                    # Fenêtre 3 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-3", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-3",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 5
            dbc.Button("Album4", id="button-france-album4", color="light", outline=True, className="mr-1"),

            # Fenêtre 4
            dbc.Modal(
                [
                    # Fenêtre 4 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 4 : Corps
                    dbc.ModalBody("Information on the album4."),
                    
                    # Fenêtre 4 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-4", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-4",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 6
            dbc.Button("Album5", id="button-france-album5", color="light", outline=True, className="mr-1"),

            # Fenêtre 5
            dbc.Modal(
                [
                    # Fenêtre 5 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 5 : Corps
                    dbc.ModalBody("Information on the album5."),
                    
                    # Fenêtre 5 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-5", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-5",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 7
            dbc.Button("Album6", id="button-france-album6", color="light", outline=True, className="mr-1"),

            # Fenêtre 6
            dbc.Modal(
                [
                    # Fenêtre 6 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 6 : Corps
                    dbc.ModalBody("Information on the album6."),
                    
                    # Fenêtre 6 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-6", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-6",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 8
            dbc.Button("Album7", id="button-france-album7", color="light", outline=True, className="mr-1"),

            # Fenêtre 7
            dbc.Modal(
                [
                    # Fenêtre 7 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 7 : Corps
                    dbc.ModalBody("Information on the album7."),
                    
                    # Fenêtre 7 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-7", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-7",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 9
            dbc.Button("Album8", id="button-france-album8", color="light", outline=True, className="mr-1"),

            # Fenêtre 8
            dbc.Modal(
                [
                    # Fenêtre 8 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 8 : Corps
                    dbc.ModalBody("Information on the album8."),
                    
                    # Fenêtre 8 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-8", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-8",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 10
            dbc.Button("Album9", id="button-france-album9", color="light", outline=True, className="mr-1"),

            # Fenêtre 9
            dbc.Modal(
                [
                    # Fenêtre 9 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 9 : Corps
                    dbc.ModalBody("Information on the album9."),
                    
                    # Fenêtre 9 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-9", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-9",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),

            # Titre 11
            dbc.Button("Album10", id="button-france-album10", color="light", outline=True, className="mr-1"),

            # Fenêtre 10
            dbc.Modal(
                [
                    # Fenêtre 10 : Titre
                    dbc.ModalHeader("Information"),

                    # Fenêtre 10 : Corps
                    dbc.ModalBody("Information on the album10."),
                    
                    # Fenêtre 10 : Pied de page
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-france-album-10", color="danger", outline=True, block=True, className="ml-auto")
                    ),
                ],
                id="modal-france-album-10",
                size="xl",
                scrollable=True,
                centered=True,
            ),

            # Separation
            html.Br(),
            html.Hr(style={"background-color":"white"}),  
        ],
        style = {"flex":1, "padding":"20px"},
    ),

    # Cote droit
    html.Div(
        [
            # Graphique
            html.Div([dcc.Graph(id="f3")], style = {}), #figure = f3
        ],
        style = {"flex":2, "display": "flex", "flex-direction": "column"},
    ),],
    style = {"display":"flex", " padding":"0px", "margin":"0px"}
)

tab_2_france = html.Div(
    [
        # Graphique 1
        html.Div([dcc.Graph(id="f1")], style = {}), #figure = f1

        # Graphique 2
        html.Div([dcc.Graph(id="f2")], style = {}), #figure = f2
    ],
    style = {"flex":2, "display": "flex", "flex-direction": "column", "padding":"0px", "margin":"0px"},
)