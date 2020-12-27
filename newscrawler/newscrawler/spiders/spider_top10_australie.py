import scrapy
from scrapy import Request
from newscrawler.items import AlbumItem


class ARIApider(scrapy.Spider):
    name = "ARIA"
    allowed_domains = ["www.aria.com.au"]
    start_urls = ['https://www.aria.com.au/charts/2010/end-of-decade-albums-chart']

    def parse(self, response):
        import re
        artists = []
        album_titles = []
        certif_UTs = []
        cpt = 0
        for album in response.xpath('//div[@class="c-chart-item_flex"]'):
            if cpt != 10:
                artists.append(album.xpath('div[@class="c-chart-item_details"/p/a[@class="c-chart-item_artist"]/text()').extract_first())
                album_titles.append(album.xpath('div[@class="c-chart-item_details"/p/a[@class="c-chart-item_title"]/text()').extract_first())
                cpt += 1 

        cpt = 0
        for album in response.xpath("//div[contains(@class, 'certif icon')]"):
            if cpt != 10 :
                certif_UTs.append(album.css("div::text").extract_first())
                cpt += 1

            for i in range(10):
                album_item = AlbumItem()
                album_item['artist'] = artists[i]
                album_item['album_title'] = album_titles[i]
                album_item['certif_UT'] = certif_UTs[i]
                yield album_item
        
