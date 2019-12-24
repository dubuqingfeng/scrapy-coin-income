# -*- coding: utf-8 -*-
import scrapy

from coinincome.items import CoinincomeItem
from coinincome.utils import calculate_unit


class ViabtcSpider(scrapy.Spider):
    name = 'viabtc'
    allowed_domains = ['viabtc.com']
    start_urls = ['https://pool.viabtc.com/']

    def parse(self, response):
        # coinname = response.xpath('//div/div[@style="max-width:160px;"]/text()')
        coinname = response.xpath('//div/div[@class="m-l-10"]/text()')
        for coin in coinname.extract():
            if coin.startswith("¥"):
                continue
            income_str_list = coin.split()
            income_hashrate_unit = income_str_list[0][0]
            standard_units = ["", "K", "M", "G", "T", "P", "E", "Z", "Y"]
            if income_hashrate_unit not in standard_units:
                income_hashrate_unit = ""
            item = CoinincomeItem()
            item['coin'] = income_str_list[3].lower()
            item['income_coin'] = float(income_str_list[2])
            item['income_hashrate_unit'] = income_hashrate_unit
            item['income_hashrate_unit_num'] = calculate_unit(income_str_list[0][0])
            item['next_income_coin'] = 0
            item['pool_name'] = self.name
            item['request_url'] = response.url
            yield item
