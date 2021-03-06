# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field



class AlbumItem(Item):
    album_title = Field()
    artist = Field()
    label = Field()
    certif_UT = Field()
    genre = Field()
    year = Field()
    price = Field()
    country = Field()
