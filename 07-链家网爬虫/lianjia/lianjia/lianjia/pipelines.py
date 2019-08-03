# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from twisted.enterprise import adbapi

class LianjiaPipeline(object):
    #
    # def __init__(self):
    #     self.fp = open("lianjia.txt", 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     self.fp.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
    #     return item
    #
    # def spider_close(self, spider):
    #     self.fp.close()

    def __init__(self, mysql_config):
        self.dbpool = adbapi.ConnectionPool(
            mysql_config['DRIVER'],
            host=mysql_config['HOST'],
            port=mysql_config['PORT'],
            user=mysql_config['USER'],
            password=mysql_config['PASSWORD'],
            db=mysql_config['DATABASE'],
            charset='utf8'
        )


    @classmethod
    def from_crawler(cls, crawler):
        # 只要重写了from_crawler方法，那么以后创建对象的时候，就会调用这个方法来获取pipline对象
        mysql_config = crawler.settings['MYSQL_CONFIG']
        return cls(mysql_config)


    def process_item(self, item, spider):
        result = self.dbpool.runInteraction(self.insert_item, item)
        result.addErrback(self.insert_error)
        return item


    def insert_item(self, cursor, item):
        sql = "insert into zufang(id,title,city,region,price,house_type,orientation,full_area," \
              "base_info,peitao,house_information,house_pushtime) values(null,%s,%s,%s,%s,%s,%s" \
              ",%s,%s,%s,%s,%s)"
        args = (item['title'],item['city'],item['region'],item['price'],item['house_type'],item['orientation'],item['full_area']
                ,item['base_info'],item['peitao'],item['house_information'],item['house_pushtime'])
        cursor.execute(sql, args)


    def insert_error(self, failure):
        print(failure)


    def close_spider(self, spider):
        self.dbpool.close()





