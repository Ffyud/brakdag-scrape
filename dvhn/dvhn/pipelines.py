# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DvhnPipeline:
    def process_item(self, article, spider):
        return article

class DvhnUpdateLink:
    def process_item(self, article, spider):
        article['link'] = "https://dvhn.nl" + article['link']
        return article
