
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
    fig_sell_price = px.scatter(df_France, x = "certif_UT", y = "price", title = "Price according to sells in " + country, hover_name = "certif_UT", hover_data=['price'])
    fig_sell_price.update_traces(mode="markers", hovertemplate=None)
    fig_sell_price.update_layout(hovermode="x unified")

    # figure 2 : Distribution of genres in the selected country
    df_genre = pd.DataFrame(list(collection.find({"country":country}, {"genre":1})))
    nbr_genre = df_genre.explode('genre')['genre'].value_counts().to_frame().reset_index()
    nbr_genre = nbr_genre.rename(columns={"index": "genre", "genre": "number"})

    fig_genre_number = px.histogram(nbr_genre, x = "genre", y= "number", title = "Distribution of genres in " + country, labels = {"number" : "Selling number", "genre" : "Genres"})

    # figure 3 : Distribution of top albums by year in the selected country
    cur = collection.find({"country":country}, {"year":1})
    df_year = pd.DataFrame(list(cur))
    fig_year = px.histogram(df_year, x = "year", title = "Distribution of top albums by year in " + country, labels = {"year" : "Years", "sum of number" : "Number of top albums"})

    return fig_sell_price, fig_genre_number, fig_year

for c in ['France', 'USA', 'UK']:
    f1, f2, f3 = get_graphes(c)
    f1.show()
    """f2.show()
    f3.show()"""



    