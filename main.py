from baby_yoda.baby_yoda.spiders.spider_top10_usa import USASpider
from baby_yoda.baby_yoda.spiders.spider_top10_france_1 import FR1Spider
from baby_yoda.baby_yoda.spiders.spider_top10_france_2 import FR2Spider
from baby_yoda.baby_yoda.spiders.spider_top10_uk import UKSpider
from webdriver import get_genre_year_price
from scrapy.crawler import CrawlerProcess
import pymongo

#get_genre_year_price()

#start all spiders
process = CrawlerProcess()
process.crawl(USASpider)
"""process.crawl(UKSpider)
process.crawl(FR1Spider)
process.crawl(FR2Spider)"""
process.start()


