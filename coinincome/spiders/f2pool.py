# -*- coding: utf-8 -*-
import scrapy


class F2poolSpider(scrapy.Spider):
    name = 'f2pool'
    allowed_domains = ['f2pool.com']
    start_urls = ['http://f2pool.com/']

    def parse(self, response):
        pass
