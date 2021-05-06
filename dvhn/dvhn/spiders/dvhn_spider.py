import scrapy


class DvhnSpiderSpider(scrapy.Spider):
    name = 'dvhn_spider'
    allowed_domains = ['dvhn.nl']
    start_urls = ['http://dvhn.nl/']

    def parse(self, response):
        pass
