import scrapy
import time
from dvhn.items import DvhnItem

class DvhnSpiderSpider(scrapy.Spider):
    name = 'dvhn_spider'
    allowed_domains = ['dvhn.nl']
    start_urls = ['https://www.dvhn.nl/groningen/stad/']

    def parse(self, response):
        article = DvhnItem()
        article['title'] = response.xpath('//a[@class="default-hero__title-link"]/text()').get()
        article['description'] = response.xpath('//p[@class="default-hero__paragraph"]/text()').get()
        article['link'] = response.xpath('//a[@class="default-hero__title-link"]/@href').get()
        article['timestamp_publicatie'] = int(round(time.time()))

        return article