# Import
import dash
import pymongo
import pandas as pd
from pymongo import MongoClient
import plotly_express as px

def get_graphes(country):

    # connect to mongo database
    client = MongoClient()
    db = client.baby_yoda
    collection = db['top_albums']

    # search the country
    cur = collection.find({"country":country}, {"price":1, "certif_UT":1})
    df_France = pd.DataFrame(list(cur))

    # figure 1 : Price according to sells in the selected country
    fig_sell_price = px.scatter(df_France, x = "certif_UT", y = "price",color_discrete_sequence=['cadetblue'], title = "Price according to sells in " + country, hover_name = "certif_UT", hover_data=['price'], labels = {"certif_UT" : "Selling number", "price" : "Prices"})
    fig_sell_price.update_traces(mode="markers", hovertemplate=None)
    fig_sell_price.update_layout({
        'plot_bgcolor': 'rgb(235, 236, 240)',
        'paper_bgcolor': 'rgb(235, 236, 240)',
        }, hovermode="x unified")

    # figure 2 : Distribution of genres in the selected country
    df_genre = pd.DataFrame(list(collection.find({"country":country}, {"genre":1})))
    nbr_genre = df_genre.explode('genre')['genre'].value_counts().to_frame().reset_index()
    nbr_genre = nbr_genre.rename(columns={"index": "genre", "genre": "number"})

    fig_genre_number = px.histogram(nbr_genre, x = "genre", y= "number", color_discrete_sequence=['cadetblue'], title = "Distribution of genres in " + country, labels = {"number" : "selling number", "genre" : "Genres"})
    fig_genre_number.update_layout({
        'plot_bgcolor': 'rgb(235, 236, 240)',
        'paper_bgcolor': 'rgb(235, 236, 240)',
        })

    # figure 3 : Distribution of top albums by year in the selected country
    cur = collection.find({"country":country}, {"year":1})
    df_year = pd.DataFrame(list(cur))
    fig_year = px.histogram(df_year, x = "year", color_discrete_sequence=['cadetblue'], title = "Distribution of top albums by year in " + country, labels = {"year" : "Years", "count" : "Number of top albums"})
    fig_year.update_layout({
        'plot_bgcolor': 'rgb(235, 236, 240)',
        'paper_bgcolor': 'rgb(235, 236, 240)',
        })


    list_sorted = collection.find({"country":country}).sort("certif_UT", -1)

    return fig_sell_price, fig_genre_number, fig_year, list(list_sorted)






    