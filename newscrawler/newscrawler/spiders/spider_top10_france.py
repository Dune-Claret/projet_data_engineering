import scrapy
from scrapy import Request
from newscrawler.items import AlbumItem

class SNEPSpider(scrapy.Spider):
    name = "snep"
    allowed_domains = ["www.snepmusique.com"]
    start_urls = ['https://snepmusique.com/les-certifications/?certification=Double%20Diamant,Triple%20Diamant,Quadruple%20Diamant&categorie=Albums']

    def parse(self, response):
            import re
            artists = []
            album_titles = []
            labels = []
            certif_UTs = []
            cpt = 0
            for album in response.xpath('//div[@class="description"]'): 
                if cpt != 5:
                    artists.append(album.xpath('div[@class="artiste"]/text()').extract_first())
                    album_titles.append(album.xpath('div[@class="titre"]/text()').extract_first())
                    labels.append(album.xpath('div[@class="editeur"]/text()').extract_first())
                    cpt += 1 

            cpt = 0
            for album in response.xpath("//div[contains(@class, 'certif icon')]"):
                if cpt != 5 :
                    certif_UTs.append(album.css("div::text").extract_first())
                    cpt += 1

            for i in range(5):
                album_item = AlbumItem()
                album_item['artist'] = artists[i]
                album_item['album_title'] = album_titles[i]
                album_item['label'] = labels[i]
                album_item['certif_UT'] = certif_UTs[i]
                yield album_item
