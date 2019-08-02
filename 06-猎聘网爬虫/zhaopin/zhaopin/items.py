# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    title = scrapy.Field()
    company  =scrapy.Field()
    city = scrapy.Field()
    edu = scrapy.Field()
    work = scrapy.Field()
    desc = scrapy.Field()
    salary = scrapy.Field()
    area = scrapy.Field()
    release_time = scrapy.Field()
