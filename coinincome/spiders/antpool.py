# -*- coding: utf-8 -*-
import json

import scrapy
from coinincome.items import CoinincomeItem


def calculate_unit(share):
    units = ["", "K", "M", "G", "T", "P", "E", "Z", "Y"]
    index = 0
    while share >= 1000:
        share = share / 1000
        index = index + 1
    return units[index]


class AntpoolSpider(scrapy.Spider):
    name = 'antpool'
    allowed_domains = ['antpool.com']
    start_urls = [
        'https://v3.antpool.com/auth/v3/index/coinList',
        'https://v3.antpool.com/lab/poolcoins'
    ]

    def parse(self, response):
        response_body = json.loads(response.body)
        if response_body['code'] == "000000":
            for coin in response_body['data']['items']:
                item = CoinincomeItem()
                item['coin'] = coin['coinType'].lower()
                # pps 收益 = 1t * 86400 / D / Coefficient * blockReward
                item['income_coin'] = coin['calculateUnit'] * 86400 / coin['networkDiff'] * coin['blockReward'] / coin[
                    'coinCoefficient']
                item['income_hashrate_unit'] = calculate_unit(coin['calculateUnit'])
                item['income_hashrate_unit_num'] = coin['calculateUnit']
                item['next_income_coin'] = 0
                item['pool_name'] = self.name
                item['request_url'] = response.url
                yield item
