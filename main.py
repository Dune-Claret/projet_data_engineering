from baby_yoda.baby_yoda.spiders.spider_top10_usa import USASpider
from baby_yoda.baby_yoda.spiders.spider_top10_france_1 import FR1Spider
from baby_yoda.baby_yoda.spiders.spider_top10_france_2 import FR2Spider
from baby_yoda.baby_yoda.spiders.spider_top10_uk import UKSpider
from baby_yoda.baby_yoda.pipelines import BabyYodaPipeline
from baby_yoda.baby_yoda.webdriver import get_genre_year_price
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import re


#settings of scrapy
settings = Settings(values={
    'BOT_NAME' : 'baby_yoda',

    'SPIDER_MODULES' : ['baby_yoda.baby_yoda.spiders'],
    'NEWSPIDER_MODULE' : 'baby_yoda.baby_yoda.spiders',
    'ITEM_PIPELINES' : {
        'baby_yoda.baby_yoda.pipelines.BabyYodaPipeline': 300,
    }
})


import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.baby_yoda
collection = db['top_albums']
collection.delete_many({})

#start all spiders
process = CrawlerProcess(settings=settings)
process.crawl(USASpider)
process.crawl(UKSpider)
process.crawl(FR1Spider)
process.crawl(FR2Spider)
process.start()

cur = collection.find({})
nbr_album = cur.count()


for album in list(cur):
    album_title = album["album_title"]
    artist = album["artist"]
    genre, year, price = get_genre_year_price(artist, album_title)
    genres = re.split('\W+', genre)
    if 'Hip' in genres:
        index = genres.index('Hip')
        genres[index] = 'Hip Hop'
        genres.remove(genres[index+1])
    collection.update_one({"album_title":album_title}, {"$set":{"genre":genres, "year" : year, "price" : price}})







