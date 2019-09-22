# -*- coding: utf-8 -*-
import json

import scrapy

from coinincome.items import CoinincomeItem


class HuobipoolSpider(scrapy.Spider):
    name = 'huobipool'
    allowed_domains = ['huobipool.com']
    start_urls = ['https://www.huobipool.com/p4/pow/product_list']

    def parse(self, response):
        response_body = json.loads(response.body)
        if response_body['code'] == 200:
            for coin in response_body['data']:
                item = CoinincomeItem()
                item['coin'] = coin['currency'].lower()
                item['income_coin'] = coin['profit']
                item['income_hashrate_unit'] = coin['profit']
                item['next_income_coin'] = 0
                item['pool_name'] = self.name
                item['request_url'] = response.url
                yield item
