import scrapy
from scrapy import Request


class RIAASpider(scrapy.Spider):
    name = "riaa"
    allowed_domains = ["www.riaa.com"]
    start_urls = ['https://www.riaa.com/gold-platinum/?tab_active=awards_by_album#search_section']

    def parse(self, response):
        import re
        cpt = 0
        for album in response.xpath('//tr[@class="table_award_row"]'):
            if cpt != 10:
                artist = album.xpath('td[@class="artists_cell"]/text()').extract_first()
                dautres_info = album.xpath('td[@class="others_cell"]/text()').extract()
                album_title = dautres_info[0]
                label = dautres_info[1]
                certif_UT = album.xpath('td[@class="others_cell format_cell"]/text()').extract_first()
                certif_UT = re.findall(r"\r\n                    (.+?)                    ",certif_UT)[0]
                cpt += 1 
                yield { "noms d'artistes" : artist, "nom d'album" : album_title, "nom de label" : label, "certification unit" : certif_UT}

