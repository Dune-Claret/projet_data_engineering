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
from requests_mongo import get_graphes

# Variables pour la page
country = 'France'
f1, f2, f3, list_albums = get_graphes(country)


tabs_styles = {
    'height': '44px'
}
tab_style = {
    'border': '0px solid rgb(105,105,105)',
    'padding': '6px',
    'fontWeight': 'bold', 
    "background-color":"rgb(105,105,105)"
}

tab_selected_style = {
    'border': '0px solid rgb(105,105,105)',
    'color': 'black',
    "background-color":"rgb(105,105,105)",
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
                html.H4("Top 10 albums in France"),

                # Break
                html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 1
                dbc.Button(list_albums[0]["album_title"], id="button-france-album1", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 1
                dbc.Modal(
                    [
                        # Fenêtre 1 : Titre
                        dbc.ModalHeader("Information"),

                        
                        # Fenêtre 1 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[0]['artist']),
                            html.Div("Album title : " + list_albums[0]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[0]['certif_UT'])), 
                            html.Div("Label : " + list_albums[0]['label']), 
                            html.Div("Country : " + list_albums[0]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[0]['genre'])),
                            html.Div("Price : " + str(list_albums[0]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[0]['year']))
                        ]),

                        
                        # Fenêtre 1 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-1", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-1",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                html.Hr(style={"background-color":"white"}),

                # Titre 2
                dbc.Button(list_albums[1]["album_title"], id="button-france-album2", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 2
                dbc.Modal(
                    [
                        # Fenêtre 2 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 2 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[1]['artist']),
                            html.Div("Album title : " + list_albums[1]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[1]['certif_UT'])), 
                            html.Div("Label : " + list_albums[1]['label']), 
                            html.Div("Country : " + list_albums[1]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[1]['genre'])),
                            html.Div("Price : " + str(list_albums[1]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[1]['year']))
                        ]),
                        
                        # Fenêtre 2 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-2", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-2",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 3
                dbc.Button(list_albums[2]["album_title"], id="button-france-album3", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 3
                dbc.Modal(
                    [
                        # Fenêtre 3 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 3 : Corps
                        dbc.ModalBody([html.Div("Artist : "+ list_albums[2]['artist']),
                            html.Div("Album title : " + list_albums[2]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[2]['certif_UT'])), 
                            html.Div("Label : " + list_albums[2]['label']), 
                            html.Div("Country : " + list_albums[2]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[2]['genre'])),
                            html.Div("Price : " + str(list_albums[2]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[2]['year']))]),
                        
                        # Fenêtre 3 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-3", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-3",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 4
                dbc.Button(list_albums[3]["album_title"], id="button-france-album4", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 4
                dbc.Modal(
                    [
                        # Fenêtre 4 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 4 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[3]['artist']),
                            html.Div("Album title : " + list_albums[3]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[3]['certif_UT'])), 
                            html.Div("Label : " + list_albums[3]['label']), 
                            html.Div("Country : " + list_albums[3]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[3]['genre'])),
                            html.Div("Price : " + str(list_albums[3]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[3]['year']))
                        ]),
                        
                        # Fenêtre 4 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-4", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-4",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 5
                dbc.Button(list_albums[4]["album_title"], id="button-france-album5", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 5
                dbc.Modal(
                    [
                        # Fenêtre 5 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 5 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[4]['artist']),
                            html.Div("Album title : " + list_albums[4]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[4]['certif_UT'])), 
                            html.Div("Label : " + list_albums[4]['label']), 
                            html.Div("Country : " + list_albums[4]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[4]['genre'])),
                            html.Div("Price : " + str(list_albums[4]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[4]['year']))
                        ]),
                        
                        # Fenêtre 5 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-5", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-5",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 6
                dbc.Button(list_albums[5]["album_title"], id="button-france-album6", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 6
                dbc.Modal(
                    [
                        # Fenêtre 6 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 6 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[5]['artist']),
                            html.Div("Album title : " + list_albums[5]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[5]['certif_UT'])), 
                            html.Div("Label : " + list_albums[5]['label']), 
                            html.Div("Country : " + list_albums[5]['country']), 
                            html.Div("Genre : " + ' '.join(e for e in list_albums[5]['genre'])),
                            html.Div("Price : " + str(list_albums[5]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[5]['year']))
                        ]),
                        
                        # Fenêtre 6 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-6", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-6",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 7
                dbc.Button(list_albums[6]["album_title"], id="button-france-album7", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 7
                dbc.Modal(
                    [
                        # Fenêtre 7 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 7 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[6]['artist']),
                            html.Div("Album title : " + list_albums[6]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[6]['certif_UT'])), 
                            html.Div("Label : " + list_albums[6]['label']), 
                            html.Div("Country : " + list_albums[6]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[6]['genre'])),
                            html.Div("Price : " + str(list_albums[6]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[6]['year']))
                        ]),
                        
                        # Fenêtre 7 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-7", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-7",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 8
                dbc.Button(list_albums[7]["album_title"], id="button-france-album8", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 8
                dbc.Modal(
                    [
                        # Fenêtre 8 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 8 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[7]['artist']),
                            html.Div("Album title : " + list_albums[7]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[7]['certif_UT'])), 
                            html.Div("Label : " + list_albums[7]['label']), 
                            html.Div("Country : " + list_albums[7]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[7]['genre'])),
                            html.Div("Price : " + str(list_albums[7]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[7]['year']))
                        ]),
                        
                        # Fenêtre 8 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-8", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-8",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 9
                dbc.Button(list_albums[8]["album_title"], id="button-france-album9", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 9
                dbc.Modal(
                    [
                        # Fenêtre 9 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 9 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[8]['artist']),
                            html.Div("Album title : " + list_albums[8]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[8]['certif_UT'])), 
                            html.Div("Label : " + list_albums[8]['label']), 
                            html.Div("Country : " + list_albums[8]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[8]['genre'])),
                            html.Div("Price : " + str(list_albums[8]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[8]['year']))
                        ]),
                        
                        # Fenêtre 9 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-9", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-9",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),

                # Titre 10
                dbc.Button(list_albums[9]["album_title"], id="button-france-album10", color="light", outline=True, className="mr-1", block=True),

                # Fenêtre 10
                dbc.Modal(
                    [
                        # Fenêtre 10 : Titre
                        dbc.ModalHeader("Information"),

                        # Fenêtre 10 : Corps
                        dbc.ModalBody([
                            html.Div("Artist : "+ list_albums[9]['artist']),
                            html.Div("Album title : " + list_albums[9]['album_title']), 
                            html.Div("Selling number : " + str(list_albums[9]['certif_UT'])), 
                            html.Div("Label : " + list_albums[9]['label']), 
                            html.Div("Country : " + list_albums[9]['country']), 
                            html.Div("Genre : " + ', '.join(e for e in list_albums[9]['genre'])),
                            html.Div("Price : " + str(list_albums[9]['price']) + "€"),
                            html.Div("Year : " + str(list_albums[9]['year']))
                        ]),
                        
                        # Fenêtre 10 : Pied de page
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-france-album-10", color="danger", outline=True, block=True, className="ml-auto")
                        ),
                    ],
                    id="modal-france-album-10",
                    size="sm",
                    scrollable=True,
                    centered=True,
                ),

                # Separation
                #html.Br(),
                html.Hr(style={"background-color":"white"}),  
            ],
            style = {"flex":1, "padding":"20px"},
        ), 
    
    # Cote droit
    html.Div(
        [
            # Graphique
            html.Div([dcc.Graph(figure = f3)], style = {})
        ],
        style = {"flex":2, "display": "flex", "flex-direction": "column"},
    )

],style = {"display":"flex", " padding":"0px", "margin":"0px"})

tab_2_france = html.Div(
    [
        html.Div([
                  html.Div([
                    dcc.Graph(figure = f1)
                  ], style={'width': '50%','display': 'inline-block', 'height' : "600px"}),
                  html.Div([
                    dcc.Graph(figure = f2)
                  ], style={'width': '50%','display': 'inline-block', 'height' : "600px"})]
        , style = {'width': '100%', 'display': 'inline-block'})
        
    ],
    style = {"flex":2, "display": "flex", "flex-direction": "column", "padding":"0px", "margin":"0px", "background-color" : "rgb(235, 236, 240)"},
)
