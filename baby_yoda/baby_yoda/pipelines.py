# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging
#from baby_yoda.webdriver import get_genre_year_price

class BabyYodaPipeline:
    collection_name = 'top_albums'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'baby_yoda')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        #self.searching_keys.append({"artist" : item['artist'], "album_title" : item['album_title']})
        
        """genre, year, price = get_genre_year_price(item['artist'], item['album_title'])
        item["genre"] = genre
        item["year"] = year
        item["price"] = price"""
        self.db[self.collection_name].insert_one(dict(item))
        logger = logging.getLogger()
        logger.warning(next(self.db[self.collection_name].find({})))
        return item