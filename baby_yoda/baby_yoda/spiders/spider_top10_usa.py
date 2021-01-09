import scrapy
from scrapy import Request
from baby_yoda.baby_yoda.items import AlbumItem
#from baby_yoda.items import AlbumItem
from scrapy.crawler import CrawlerProcess


class USASpider(scrapy.Spider):
    name = "USA"
    allowed_domains = ["www.riaa.com"]
    start_urls = ['https://www.riaa.com/gold-platinum/?tab_active=awards_by_album#search_section']

    def parse(self, response):
        import re
        cpt = 0
        for album in response.xpath('//tr[@class="table_award_row"]'):
            if cpt != 10:
                album_item = AlbumItem()
                album_item['artist'] = album.xpath('td[@class="artists_cell"]/text()').extract_first()
                other_info = album.xpath('td[@class="others_cell"]/text()').extract()
                album_item['album_title'] = other_info[0]
                album_item['label'] = other_info[1]
                certif_UT = album.xpath('td[@class="others_cell format_cell"]/text()').extract_first()
                album_item['certif_UT'] = re.findall(r"\r\n                    (.+?)                    ",certif_UT)[0]
                album_item['certif_UT'] += "000000"
                album_item['country'] = "USA"
                cpt += 1 
                yield album_item

if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(USASpider)
  process.start()