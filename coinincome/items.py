# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinincomeItem(scrapy.Item):
    pool_name = scrapy.Field()
    coin = scrapy.Field()
    income = scrapy.Field()
    income_coin = scrapy.Field()
    next_income_coin = scrapy.Field()
    income_hashrate_unit = scrapy.Field()
    request_url = scrapy.Field()
    pass
