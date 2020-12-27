import scrapy
from scrapy import Request

class labelspider(scrapy.Spider):
    name="label"
    allowed_domains = ["www.discogs.com"]
    start_urls = ['https://www.discogs.com/fr/Taylor-Swift-1989/master/750386']

    def parse(self, response):
        import re
        for label in response.xpath("//tr[contains(@class, 'card r_tr main release')]"):
        #for label in response.xpath('//div[@class="section m_versions toggle_section toggle_section_remember toggle_section_collapsed"/p/a[@class="section_content toggle_section_content"/p/a[@class="cards table_responsive layout_text-only"]'):
            label_item = label.css("tr::text").extract_first()
            #label_item = label.css("td[@class='label has_header']::text").extract_first()
            yield label_item

