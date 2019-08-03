# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 行政区
    region = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 面积
    full_area = scrapy.Field()
    # 基本信息
    base_info = scrapy.Field()
    # 配套设施
    peitao = scrapy.Field()
    # 房源描述
    house_information = scrapy.Field()
    # 房源上架时间
    house_pushtime = scrapy.Field()





