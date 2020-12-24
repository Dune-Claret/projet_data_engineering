import scrapy
from scrapy import Request


class ARIApider(scrapy.Spider):
    name = "ARIA"
    allowed_domains = ["www.aria.com.au"]
    start_urls = ['https://www.aria.com.au/charts/2010/end-of-decade-albums-chart']

    def parse(self, response):
        import re
        cpt = 0
        for album in response.xpath('//div[@class="c-chart-item_flex"]'):
            if cpt != 10:
                #artist = album.xpath('td[@class="artists_cell"]/text()').extract_first()
                album_title = album.xpath('div[@class="c-chart-item_details"/p/a[@class="c-chart-item_title"]/text()').extract_first()
                
                cpt += 1 
                #yield { "noms d'artistes" : artist, "nom d'album" : album_title, "nom de label" : label, "certification unit" : certif_UT}
                yield {"nom d'album" : album_title}
