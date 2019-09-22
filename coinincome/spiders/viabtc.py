# -*- coding: utf-8 -*-
import scrapy


class ViabtcSpider(scrapy.Spider):
    name = 'viabtc'
    allowed_domains = ['viabtc.com']
    start_urls = ['http://pool.viabtc.com/']

    def parse(self, response):
        pass
