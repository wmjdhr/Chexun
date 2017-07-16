# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Chexun.items import ChexunUrlItem, ChexunBrandItem


class CarmodelUrlSpider(CrawlSpider):
    name = 'carmodel_url'
    start_urls = [
        'http://auto.chexun.com/search-a0-b0-c0-d0-e0-f0-g0-h0-i0:0.html'
    ]

    # rules = (
    #     Rule(LinkExtractor(allow=r'data'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        item = ChexunBrandItem()

        # locate info (as a dict)
        info_pattern = re.compile('var series = (.+?);')
        info = re.findall(response.body, info_pattern)[0]
        info_dict = dict(info)
        brand = info_dict.get('brandMap')
        company = info_dict.get('companyMap')
        series = info_dict.get('seriesMap')
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
