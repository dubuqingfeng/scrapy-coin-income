# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class CoinincomePipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '', 'bank', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO xxx (pool_name, coin, income_coin, income_coin_unit)
                            VALUES (%s, %s, %s, %s )""",
                                (item['name'].encode('utf-8'),
                                 item[''].encode('utf-8'),
                                 item['phone'].encode('utf-8'),
                                 item['address'].encode('utf-8')))
            self.conn.commit()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        return item
