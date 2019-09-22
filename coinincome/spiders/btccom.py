# -*- coding: utf-8 -*-
import scrapy
import json

###
# 实际上需要按缓存区分？
# https://pool.btc.com/v1/coins-income
# Main
from coinincome.items import CoinincomeItem


class BtccomSpider(scrapy.Spider):
    name = 'btccom'
    allowed_domains = ['btc.com']
    start_urls = [
        'https://pool.btc.com/v1/coins-income',
        'https://us-pool.api.btc.com/v1/coins-income',
        'https://eu-pool.api.btc.com/v1/coins-income'
    ]

    def parse(self, response):
        response_body = json.loads(response.body)
        if response_body['err_no'] == 0:
            for coin in response_body['data']:
                item = CoinincomeItem()
                item['coin'] = coin.lower()
                item['income_coin'] = response_body['data'][coin]['income_coin']
                item['income_hashrate_unit'] = response_body['data'][coin]['income_hashrate_unit']
                item['next_income_coin'] = response_body['data'][coin]['next_income_coin']
                item['pool_name'] = self.name
                item['request_url'] = response.url
                yield item
