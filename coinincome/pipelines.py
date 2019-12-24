# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import math

import pymysql
from twisted.enterprise import adbapi


class CoinincomePipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLTwistedPipeline(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        db_pool = adbapi.ConnectionPool("pymysql", host=settings["MYSQL_HOST"], db=settings["MYSQL_DBNAME"],
                                        user=settings["MYSQL_USER"], password=settings["MYSQL_PASSWORD"],
                                        charset="utf8", cursorclass=pymysql.cursors.DictCursor,
                                        use_unicode=True)
        return cls(db_pool)

    def process_item(self, item, spider):
        if self.db_pool is not None:
            self.db_pool.runInteraction(self.insert_item, item)

    def insert_item(self, cursor, item):
        insert_sql = """INSERT INTO pool_coin_incomes(pool_name, coin, income_coin, income_hashrate_unit, 
                            income_hashrate_unit_num, updated_at) VALUES 
                            (%s, %s, %s, %s, %s, now()) ON DUPLICATE KEY UPDATE pool_name = %s, coin = %s, 
                             income_coin = %s, income_hashrate_unit = %s, income_hashrate_unit_num = %s, 
                             updated_at = now();"""
        params = (item['pool_name'].encode('utf-8'), item['coin'].encode('utf-8'),
                  item['income_coin'], item['income_hashrate_unit'].encode('utf-8'),
                  item['income_hashrate_unit_num'],
                  item['pool_name'].encode('utf-8'), item['coin'].encode('utf-8'),
                  item['income_coin'], item['income_hashrate_unit'].encode('utf-8'), item['income_hashrate_unit_num'])
        cursor.execute(insert_sql, params)
        sql = "SELECT * FROM pool_coin_income_history WHERE pool_name = %s and coin = %s order by " \
              "created_at desc limit 1;"
        cursor.execute(sql, (item['pool_name'].encode('utf-8'), item['coin'].encode('utf-8')))
        result = cursor.fetchall()
        for row in result:
            if math.isclose(row['income_coin'], item['income_coin'], rel_tol=1e-6):
                return
            else:
                if row['request_url'] != item['request_url']:
                    text = "diff:coin:%s:prev:%s:time:%s:url:'%s':now:%s:url:'%s'" % (
                        item['coin'], row['income_coin'], row['created_at'], row['request_url'], item['income_coin'],
                        item['request_url'])
                    print(text)
                else:
                    text = "diff:coin:%s:prev:%s:url:'%s':now:%s" % (
                        item['coin'], row['income_coin'], row['request_url'], item['income_coin'])
                    print(text)
        insert_history_sql = """INSERT INTO pool_coin_income_history(pool_name, coin, request_url, income_coin, 
        income_hashrate_unit, created_at)  VALUES (%s, %s, %s, %s, %s, now());"""
        cursor.execute(insert_history_sql, (item['pool_name'].encode('utf-8'), item['coin'].encode('utf-8'),
                                            item['request_url'].encode('utf-8'),
                                            item['income_coin'], item['income_hashrate_unit'].encode('utf-8'),))
