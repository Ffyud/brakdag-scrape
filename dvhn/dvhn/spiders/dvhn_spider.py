import scrapy


class DvhnSpiderSpider(scrapy.Spider):
    name = 'dvhn_spider'
    allowed_domains = ['dvhn.nl']
    start_urls = ['https://www.dvhn.nl/groningen/stad/']

    def parse(self, response):
        title = response.xpath('//a[@class="default-hero__title-link"]/text()').get()
        descr = response.xpath('//p[@class="default-hero__paragraph"]/text()').get()
        link = response.xpath('//a[@class="default-hero__title-link"]/@href').get()
        return {"title": title, "description": descr, "link": "https://dvhn.nl" + link}
