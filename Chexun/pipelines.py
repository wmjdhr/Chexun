# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.engine import create_engine
from datetime import date
import json

class MSSQLPipeline_CarModel(object):

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.import_time = date.today()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            connection_string=crawler.settings.get('CONNECTION_STRING_CHEXUN')
        )

    def open_spider(self, spider):
        self.engine = create_engine(self.connection_string)

    def process_item(self, item, spider):
        if spider.name == 'carmodel_index':
            with open('temp.pkl', 'r') as f:
                content = json.load(f)
                print content
            return item
        # if spider.name == 'carmodel_url':
        #     sql = "insert into STG.CARMODEL_BRAND (BRAND, BRAND_ID, BRAND_NAME, BRAND_NAME_ENG, LAST_UPDATE)" \
        #           " select '%s', '%s', '%s', '%s', '%s'" % (item.get('brand'), item.get('brandId'), item.get('brandName'), item.get('englishName'), self.import_time)
        #     self.engine.execute(sql)
        #     return item