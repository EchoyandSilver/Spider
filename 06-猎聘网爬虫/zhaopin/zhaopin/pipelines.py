# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from twisted.enterprise import adbapi

class ZhaopinPipeline(object):
    # 写入json文件
    # def __init__(self):
    #     self.fp = open("jobs.txt",'w',encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     self.fp.write(json.dumps(dict(item),ensure_ascii=False) + "\n")
    #     return item
    #
    # def close_spider(self,spider):
    #     self.fp.close()

    # 写入数据库
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
        sql = "insert into joblist(id,title,area,release_time,company,edu,worktime,descContent,salary) values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (item['title'],item['area'],item['release_time'], item['company'], item['edu'], item['work'], item['desc'], item['salary'])
        cursor.execute(sql,args)

    def insert_error(self,failure):
        print("="*30)
        print(failure)
        print("="*30)

    def close_spider(self,spider):
        self.dbpool.close()








