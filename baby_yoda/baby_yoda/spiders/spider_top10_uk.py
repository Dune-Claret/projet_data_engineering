import scrapy
from scrapy import Request
from baby_yoda.baby_yoda.items import AlbumItem
#from baby_yoda.items import AlbumItem


class UKSpider(scrapy.Spider):
    name = "uk"
    allowed_domains = ["www.businessinsider.com"]
    start_urls = ['https://www.businessinsider.com/50-best-selling-albums-all-time-2016-9?IR=T#1-eagles-their-greatest-hits-1971-1975-50']

    def parse(self, response):
        import re
        cpt = 0
        for album in response.xpath('//div[@class="slide-layout clearfix"]'):
            cpt += 1 
            album_item = AlbumItem()
            if cpt > 40:
                title_artist = album.xpath('div[@class="slide-title clearfix"]/h2/text()').extract_first()
                artist, album_title = title_artist.split(' — ')
                album_item['artist'] = artist.split(". ")[1]
                album_item['album_title'] = re.findall(r"\"(.+?)\"",album_title)[0]
                album_item['certif_UT'] = album.xpath('p/text()').extract_first()[:2] + "000000"
                label = album.xpath('figure[@class="figure image-figure-image "]/span/span/text()').extract_first()
                album_item['label'] = re.findall(r"\n                                                (.+?)\n                                              ", label)[0]
                album_item['country'] = "UK"
                yield album_item
