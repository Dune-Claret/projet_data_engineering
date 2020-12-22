import scrapy
from scrapy import Request


class SNEPSpider(scrapy.Spider):
    name = "snep"
    allowed_domains = ["www.snepmusique.com"]
    start_urls = ['https://snepmusique.com/les-certifications/?certification=Double%20Diamant,Triple%20Diamant,Quadruple%20Diamant&categorie=Albums']

    def parse(self, response):
            import re
            cpt = 0
            for album in response.xpath('//div[@class="description"]'): 
                if cpt != 10:
                    artist = album.xpath('div[@class="artiste"]/text()').extract_first()
                    album_title = album.xpath('div[@class="titre"]/text()').extract_first()
                    label = album.xpath('div[@class="editeur"]/text()').extract_first()
                    cpt += 1 
                    yield { "Artist : " : artist, "Album : " : album_title, "Label : " : label}

            cpt = 0
            for album in response.xpath("//div[contains(@class, 'certif icon')]"):
                if cpt != 10 :
                    certif_UT = album.css("div::text").extract_first()
                    cpt += 1

                    yield {"Certification unit" : certif_UT}