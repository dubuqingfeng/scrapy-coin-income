# -*- coding: utf-8 -*-
import scrapy


class OkpoolSpider(scrapy.Spider):
    name = 'okpool'
    allowed_domains = ['okpool.com']
    start_urls = ['http://okpool.com/']

    def parse(self, response):
        pass
