# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Imports de fichiers en local
from uk import (correlation_alert_component_uk,
                                correlation_france_usa_uk,
                                country_selection,
                                graph_france_usa_uk,
                                heatmap_france_usa_uk,
                                lineplot_graph, pageUk)
from usa import (graph_line_desktop_manual_country_range,
                                 graph_line_subjects_country_range,
                                 graph_pie_subjects_country_year,
                                 pageUsa)
from navigation_bar import navigationBar
from france import (dropdown_continents, dropdown_countries,
                              graph_bar_france, graph_line_france_group,
                              graph_map_france, graph_pie_france_group,
                              pageFrance, rank_france_group)

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
    
    # FRANCE - Interactivite: Changement d'annee sur la page 'France'
    @app.callback(
        [dash.dependencies.Output('graph-bar-france', 'figure'),
        dash.dependencies.Output('graph-map-france', 'figure'),
        dash.dependencies.Output('label-year-france', 'children')],
        [dash.dependencies.Input('dropdown-france-year', 'value')]
    )
    def change_year(year):
        return [graph_bar_france(year), graph_map_france(year), "Year {}".format(year)]

    # FRANCE - Interactivite: Choix de groupe/region
    @app.callback(
        [dash.dependencies.Output('dropdown-france-group-location', 'options'),
        dash.dependencies.Output('dropdown-france-group-location', 'value')],
        [dash.dependencies.Input('radioitems-france-group', 'value')]
    )
    def group_input(group_type):
        return [dropdown_countries, "France"] if group_type == "Countries" else [dropdown_continents, "Europe"]

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

    # FRANCE - Interactivite: Indicateur des annees pour le range slider
    @app.callback(
        dash.dependencies.Output("label-france-group-graph", "children"),
        dash.dependencies.Input("slider-france-group-graph", "value")
    )
    def change_range_slider(values):
        return "From {} to {}:".format(values[0], values[1])

    # FRANCE - Interactivite: Creation du graphique pour une region specifique
    @app.callback(
        dash.dependencies.Output("lineplot-france-graph", "figure"),
        [dash.dependencies.Input('slider-france-group-graph', "value"),
        dash.dependencies.Input('radioitems-france-group', 'value'),
        dash.dependencies.Input('dropdown-france-group-location', 'value')]
    )
    def create_graph_group(interval, group_type, location):
        return graph_line_france_group(interval[0], interval[1], group_type, location)

    # FRANCE - Interactivite: Creation du graphique camembert, du classement par rapport au slider des annees
    @app.callback(
        [dash.dependencies.Output("label-france-miscellaneous", "children"),
        dash.dependencies.Output("piechart-france-miscellaneous", "figure"),
        dash.dependencies.Output("ranking-france-miscellaneous", "children"),
        dash.dependencies.Output("ranking-text-france-miscellaneous", "children")],
        [dash.dependencies.Input("slider-france-miscellaneous-graph", "value"),
        dash.dependencies.Input('radioitems-france-group', 'value'),
        dash.dependencies.Input('dropdown-france-group-location', 'value')]
    )
    def change_slider(value, group_type, location):
        # For the rank widget
        #rank, n = rank_france_group(value, group_type, location)
        #ranktxt =  "\n among " + ("countries" if group_type == "Countries" else "continents")

        #return "During the year {}".format(value), graph_pie_france_group(value, group_type, location), "{}/{}".format(rank, n), ranktxt
        return 0

    # USA - Interactivite: Creation du graphique stacked area des activites, camembert des activites, lineplot
    # des types d'activite (bureautique ou manuel)
    @app.callback(
        [dash.dependencies.Output("lineplot-subjects-usa", "figure"),
        dash.dependencies.Output("piecharts-subjects-usa", "figure"),
        dash.dependencies.Output("label-year-piechart-usa", "children"),
        dash.dependencies.Output("lineplot-activity-usa", "figure")],
        [dash.dependencies.Input("input-country-usa", "value"),
        dash.dependencies.Input("input-range-year-usa", "value"),
        dash.dependencies.Input("input-sex-usa", "value"),
        dash.dependencies.Input("input-activity-usa", "value"),
        dash.dependencies.Input("input-year-usa", "value")]
    )
    def update_inputs_usa(country, year_range, sex, year):
        return 0 #[
            #graph_line_subjects_country_range(year_range[0], year_range[1], country, sex),
            #graph_pie_subjects_country_year(year, country, sex),
            #"You selected the year {}".format(year),
            #graph_line_desktop_manual_country_range(year_range[0], year_range[1], country)
        #]

    # UK - Interactivite: Creation du graphique lineplot, de la correlation de l'obesite par rapport aux activites
    # bureautiques ou manuelles
    @app.callback(
        [dash.dependencies.Output("graph-lineplot-correlationD-uk", "figure"),
        dash.dependencies.Output("graph-lineplot-correlationM-uk", "figure"),
        dash.dependencies.Output("alert-correlationD-uk", "children"),
        dash.dependencies.Output("alert-correlationM-uk", "children")],
        [dash.dependencies.Input("dropdown-country-uk", "value"),
        dash.dependencies.Input("radio-corr-type-uk", "value")]
    )
    def change_country(country, corrtype):
        corrD = correlation_france_usa_uk(country, "D", corrtype)
        corrM = correlation_france_usa_uk(country, "M", corrtype)
        return (graph_france_usa_uk(country, "D", corrtype),
        graph_france_usa_uk(country, "M", corrtype),
        correlation_alert_component_uk(country, "D", corrD, corrtype),
        correlation_alert_component_uk(country, "M", corrM, corrtype))

    # UK - Interactivite: Changement du type de graphique ('lineplot', 'heatmap'), apparition 
    # de la selection de pays seulement lorsque le type de visualisation est le 'lineplot'.
    @app.callback(
        [dash.dependencies.Output("graphs-uk", "children"),
        dash.dependencies.Output("ui-dropdown-country-uk", "children")],
        [dash.dependencies.Input("radio-graph-type-uk", "value"),
        dash.dependencies.Input("radio-corr-type-uk", "value")]
    )
    def change_graph_type(gtype, corrtype):

        heatmap = dcc.Graph(figure=heatmap_france_usa_uk(corrtype))

        return (heatmap, None) if gtype == "heatmap" else (lineplot_graph, country_selection)

    # Titre de l'application
    app.title = "World's top albums"

    # Execute l'application Dash sur un serveur web local
    app.run_server(debug=False)

    pass

