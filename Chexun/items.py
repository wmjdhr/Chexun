# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ChexunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ChexunUrlItem(scrapy.Item):
    url = Field()


class ChexunBrandItem(scrapy.Item):
    brand = Field()
    brandId = Field()
    brandName = Field()
    englishName = Field()

class ChexunTemp(scrapy.Item):
    brand = Field()
    company = Field()
    series = Field()
