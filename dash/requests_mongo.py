# Import
import dash
import pymongo
import pandas as pd
from pymongo import MongoClient
import plotly_express as px

def get_graphes(country):
    client = MongoClient()
    db = client.baby_yoda
    collection = db['top_albums']

    cur = collection.find({"country":country}, {"price":1, "certif_UT":1})
    df_France = pd.DataFrame(list(cur))

    fig_sell_price = px.scatter(df_France, x = "certif_UT", y = "price", title = "Price = f(sells) in " + country)

    df_genre = pd.DataFrame(list(collection.find({"country":country}, {"genre":1})))
    nbr_genre = df_genre.explode('genre')['genre'].value_counts().to_frame().reset_index()
    nbr_genre = nbr_genre.rename(columns={"index": "genre", "genre": "number"})

    fig_genre_number = px.histogram(nbr_genre, x = "genre", y= "number", title = "Distribution of genres in " + country, labels = {"number" : "Selling number", "genre" : "Genres"})

    cur = collection.find({"country":country}, {"year":1})
    df_year = pd.DataFrame(list(cur))
    fig_year = px.histogram(df_year, x = "year", title = "Distribution of albums in " + country, labels = {"year" : "Years", "sum of number" : "Number of top albums"})

    """cur = collection.find( { "$or": [ { "country": "UK"}, { "country": "USA" } ] })
    print(list(cur))"""

    return fig_sell_price, fig_genre_number, fig_year





    