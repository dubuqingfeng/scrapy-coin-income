# -*- coding: utf-8 -*-
import scrapy


class AntpoolSpider(scrapy.Spider):
    name = 'antpool'
    allowed_domains = ['antpool.com']
    start_urls = ['http://antpool.com/']

    def parse(self, response):
        pass
