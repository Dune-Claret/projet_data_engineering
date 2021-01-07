
import pymongo
import pandas as pd
from pymongo import MongoClient
import plotly_express as px

client = MongoClient()
db = client.baby_yoda
collection = db['top_albums']

"""cur = collection.find({"country":"France"}, {"price":1, "certif_UT":1})
df_France = pd.DataFrame(list(cur))

fig = px.scatter(df_France, x = "certif_UT", y = "price")
fig.show()"""

df_genre = pd.DataFrame(list(collection.find({}, {"genre":1})))
df_genre= df_genre.iloc[:9]
print(df_genre["_id"].tolist())
"""genres = [elem[k] for k in range(len(elem)) for elem in df_genre["genre"].tolist()]
print(df_genre["genre"].tolist())"""