#!/bin/bash
cd coinincome
scrapy runspider spiders/btccom.py
scrapy runspider spiders/poolin.py
scrapy runspider spiders/huobipool.py
scrapy runspider spiders/antpool.py
scrapy runspider spiders/sparkpool.py
