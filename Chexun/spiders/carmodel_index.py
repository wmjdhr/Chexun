# -*- coding: utf-8 -*-
import scrapy
import re
from Chexun.items import ChexunTemp


class CarmodelIndexSpider(scrapy.Spider):
    name = 'carmodel_index'
    start_urls = [
        'http://auto.chexun.com/search-a0-b0-c0-d0-e0-f0-g0-h0-i0:0.html'
    ]

    def parse(self, response):
        i = ChexunTemp()
        content = response.body.decode('utf-8')
        pattern = re.compile('var series = (.+?);')
        i['content'] = re.search(pattern, content).group(1)
        return i
