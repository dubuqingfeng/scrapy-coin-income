# -*- coding: utf-8 -*-
import json

import scrapy

from coinincome.items import CoinincomeItem


class SparkpoolSpider(scrapy.Spider):
    name = 'sparkpool'
    allowed_domains = ['sparkpool.com']
    start_urls = ['https://www.sparkpool.com/v1/pool/stats?pool=SPARK_POOL_CN']

    def parse(self, response):
        response_body = json.loads(response.body)
        if response_body['code'] == 200:
            for coin in response_body['data']:
                item = CoinincomeItem()
                item['coin'] = coin['currency'].lower()
                item['income_coin'] = coin['income']
                item['income_hashrate_unit'] = coin['incomeHashrate']
                item['next_income_coin'] = 0
                item['pool_name'] = self.name
                item['request_url'] = response.url
                yield item
