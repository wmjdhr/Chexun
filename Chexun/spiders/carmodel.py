# -*- coding: utf-8 -*-
import scrapy


class CarmodelSpider(scrapy.Spider):
    name = 'carmodel'
    allowed_domains = ['www.chexun.com']
    start_urls = ['http://www.chexun.com/']

    def parse(self, response):
        pass
