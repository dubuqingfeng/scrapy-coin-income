# -*- coding: utf-8 -*-
import scrapy


class F2poolSpider(scrapy.Spider):
    name = 'f2pool'
    allowed_domains = ['f2pool.com']
    start_urls = ['https://f2pool.com/']

    def parse(self, response):
        for project in response.xpath('//div/div/section/div/div/table/tbody/a[@class="btn-calculator"]'):
            if project.extract() != '#':
                print('https://www.f2pool.com%s' % project.extract())
