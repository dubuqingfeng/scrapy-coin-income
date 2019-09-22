# -*- coding: utf-8 -*-
import scrapy


class HuobipoolSpider(scrapy.Spider):
    name = 'huobipool'
    allowed_domains = ['huobipool.com']
    start_urls = ['http://huobipool.com/']

    def parse(self, response):
        pass
