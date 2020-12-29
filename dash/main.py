# Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Imports de fichiers en local
from analytics_page import (correlation_alert_component_analytics,
                                correlation_page_two_page_one_analytics,
                                country_selection,
                                graph_page_two_page_one_analytics,
                                heatmap_page_two_page_one_analytics,
                                lineplot_graph, pageAnalytics)
from page1 import (graph_line_desktop_manual_country_range,
                                 graph_line_subjects_country_range,
                                 graph_pie_subjects_country_year,
                                 pageOne)
from navigation_bar import navigationBar
from page2 import (dropdown_continents, dropdown_countries,
                              graph_bar_page_two, graph_line_page_two_group,
                              graph_map_page_two, graph_pie_page_two_group,
                              pageTwo, rank_page_two_group)

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
        if pathname == '/page2':
            return pageTwo
        elif pathname == '/page1':
            return pageOne 
        elif pathname == '/analytics':
            return pageAnalytics    
        else:
            return pageTwo
    
    # PAGE2 - Interactivite: Changement d'annee sur la page 'page2'
    @app.callback(
        [dash.dependencies.Output('graph-bar-page-two', 'figure'),
        dash.dependencies.Output('graph-map-page-two', 'figure'),
        dash.dependencies.Output('label-year-page-two', 'children')],
        [dash.dependencies.Input('dropdown-page-two-year', 'value')]
    )
    def change_year(year):
        return [graph_bar_page_two(year), graph_map_page_two(year), "Year {}".format(year)]

    # PAGE2 - Interactivite: Choix de groupe/region
    @app.callback(
        [dash.dependencies.Output('dropdown-page-two-group-location', 'options'),
        dash.dependencies.Output('dropdown-page-two-group-location', 'value')],
        [dash.dependencies.Input('radioitems-page-two-group', 'value')]
    )
    def group_input(group_type):
        return [dropdown_countries, "France"] if group_type == "Countries" else [dropdown_continents, "Europe"]

    # PAGE2 - Interactivite: Ouverture fenetre pour region specifique
    @app.callback(
        [dash.dependencies.Output("modal-page-two-group", "is_open"),
        dash.dependencies.Output("header-page-two-group", "children")],
        [dash.dependencies.Input("button-page-two-group", "n_clicks"),
        dash.dependencies.Input("close-modal-page-two-group", "n_clicks"),
        dash.dependencies.Input("dropdown-page-two-group-location", "value")],
        [dash.dependencies.State("modal-page-two-group", "is_open")]
    )
    def open_modal(n1, n2, location, is_open):
        if n1 or n2:
            return not is_open, location

        return is_open, None

    # PAGE2 - Interactivite: Ouverture fenetre pour region specifique bis
    @app.callback(
        dash.dependencies.Output("button-page-two-group", "n_clicks"),
        dash.dependencies.Input("close-modal-page-two-group", "n_clicks"),
    )
    def reset_button_submit(n_clicks_close):
        return None

    # PAGE2 - Interactivite: Indicateur des annees pour le range slider
    @app.callback(
        dash.dependencies.Output("label-page-two-group-graph", "children"),
        dash.dependencies.Input("slider-page-two-group-graph", "value")
    )
    def change_range_slider(values):
        return "From {} to {}:".format(values[0], values[1])

    # PAGE2 - Interactivite: Creation du graphique pour une region specifique
    @app.callback(
        dash.dependencies.Output("lineplot-page-two-graph", "figure"),
        [dash.dependencies.Input('slider-page-two-group-graph', "value"),
        dash.dependencies.Input('radioitems-page-two-group', 'value'),
        dash.dependencies.Input('dropdown-page-two-group-location', 'value')]
    )
    def create_graph_group(interval, group_type, location):
        return graph_line_page_two_group(interval[0], interval[1], group_type, location)

    # PAGE2 - Interactivite: Creation du graphique camembert, du classement par rapport au slider des annees
    @app.callback(
        [dash.dependencies.Output("label-page-two-miscellaneous", "children"),
        dash.dependencies.Output("piechart-page-two-miscellaneous", "figure"),
        dash.dependencies.Output("ranking-page-two-miscellaneous", "children"),
        dash.dependencies.Output("ranking-text-page-two-miscellaneous", "children")],
        [dash.dependencies.Input("slider-page-two-miscellaneous-graph", "value"),
        dash.dependencies.Input('radioitems-page-two-group', 'value'),
        dash.dependencies.Input('dropdown-page-two-group-location', 'value')]
    )
    def change_slider(value, group_type, location):
        # For the rank widget
        #rank, n = rank_page_two_group(value, group_type, location)
        #ranktxt =  "\n among " + ("countries" if group_type == "Countries" else "continents")

        #return "During the year {}".format(value), graph_pie_page_two_group(value, group_type, location), "{}/{}".format(rank, n), ranktxt
        return 0

    # PAGE1 - Interactivite: Creation du graphique stacked area des activites, camembert des activites, lineplot
    # des types d'activite (bureautique ou manuel)
    @app.callback(
        [dash.dependencies.Output("lineplot-subjects-page-one", "figure"),
        dash.dependencies.Output("piecharts-subjects-page-one", "figure"),
        dash.dependencies.Output("label-year-piechart-page-one", "children"),
        dash.dependencies.Output("lineplot-activity-page-one", "figure")],
        [dash.dependencies.Input("input-country-page-one", "value"),
        dash.dependencies.Input("input-range-year-page-one", "value"),
        dash.dependencies.Input("input-sex-page-one", "value"),
        dash.dependencies.Input("input-activity-page-one", "value"),
        dash.dependencies.Input("input-year-page-one", "value")]
    )
    def update_inputs_page_one(country, year_range, sex, year):
        return 0 #[
            #graph_line_subjects_country_range(year_range[0], year_range[1], country, sex),
            #graph_pie_subjects_country_year(year, country, sex),
            #"You selected the year {}".format(year),
            #graph_line_desktop_manual_country_range(year_range[0], year_range[1], country)
        #]

    # ANALYTICS - Interactivite: Creation du graphique lineplot, de la correlation de l'obesite par rapport aux activites
    # bureautiques ou manuelles
    @app.callback(
        [dash.dependencies.Output("graph-lineplot-correlationD-analytics", "figure"),
        dash.dependencies.Output("graph-lineplot-correlationM-analytics", "figure"),
        dash.dependencies.Output("alert-correlationD-analytics", "children"),
        dash.dependencies.Output("alert-correlationM-analytics", "children")],
        [dash.dependencies.Input("dropdown-country-analytics", "value"),
        dash.dependencies.Input("radio-corr-type-analytics", "value")]
    )
    def change_country(country, corrtype):
        corrD = correlation_page_two_page_one_analytics(country, "D", corrtype)
        corrM = correlation_page_two_page_one_analytics(country, "M", corrtype)
        return (graph_page_two_page_one_analytics(country, "D", corrtype),
        graph_page_two_page_one_analytics(country, "M", corrtype),
        correlation_alert_component_analytics(country, "D", corrD, corrtype),
        correlation_alert_component_analytics(country, "M", corrM, corrtype))

    # ANALYTICS - Interactivite: Changement du type de graphique ('lineplot', 'heatmap'), apparition 
    # de la selection de pays seulement lorsque le type de visualisation est le 'lineplot'.
    @app.callback(
        [dash.dependencies.Output("graphs-analytics", "children"),
        dash.dependencies.Output("ui-dropdown-country-analytics", "children")],
        [dash.dependencies.Input("radio-graph-type-analytics", "value"),
        dash.dependencies.Input("radio-corr-type-analytics", "value")]
    )
    def change_graph_type(gtype, corrtype):

        heatmap = dcc.Graph(figure=heatmap_page_two_page_one_analytics(corrtype))

        return (heatmap, None) if gtype == "heatmap" else (lineplot_graph, country_selection)

    # Titre de l'application
    app.title = "Dashboard"

    # Execute l'application Dash sur un serveur web local
    app.run_server(debug=False)

    pass

