# -*- coding: utf-8 -*-
import json

import scrapy

from coinincome.items import CoinincomeItem
from coinincome.utils import calculate_unit


class F2poolSpider(scrapy.Spider):
    name = 'f2pool'
    allowed_domains = ['f2pool.com']
    start_urls = ['https://www.f2pool.com/']

    def parse(self, response):

        for coin_config in response.xpath(
                '//tr[contains(@class, "row-common")]/td/a[contains(@class, "btn-calculator")]/@data-config'):
            if coin_config.extract() != '':
                coin = json.loads(coin_config.extract())
                item = CoinincomeItem()
                item['coin'] = coin['currency'].lower()
                item['income_coin'] = float(coin['estimatedProfit'])
                item['income_hashrate_unit'] = coin['scale']
                item['income_hashrate_unit_num'] = calculate_unit(coin['scale'])
                item['next_income_coin'] = 0
                item['pool_name'] = self.name
                item['request_url'] = response.url
                yield item
