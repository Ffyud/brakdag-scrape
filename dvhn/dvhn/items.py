# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DvhnItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    timestamp_publicatie = scrapy.Field()
