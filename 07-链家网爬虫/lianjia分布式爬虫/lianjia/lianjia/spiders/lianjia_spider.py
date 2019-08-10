# -*- coding: utf-8 -*-
import scrapy
from ..items import LianjiaItem
import json
from functools import reduce
import re

from scrapy_redis.spiders import RedisSpider


class LianjiaSpiderSpider(RedisSpider):
    name = 'lianjia_spider'
    allowed_domains = ['lianjia.com']
    #start_urls = ['https://www.lianjia.com/city/']
    redis_key = 'lianjia'

    def parse(self, response):
        city_tags = response.css('.city_list_ul a')
        for city_tag in city_tags:
            city = city_tag.css('::text').get()
            city_url = city_tag.css('::attr(href)').get()
            item = LianjiaItem(city=city)
            yield scrapy.Request(city_url + "zufang/", callback=self.parse_region_list,meta={"item": item})


    def parse_region_list(self, response):
        # 解析行政区的url
        item = response.meta.get('item')
        region_tags = response.css('ul[data-target="area"] a')
        for region_tag in region_tags:
            region_url = region_tag.css('::attr(href)').get()
            region_name = region_tag.css('::text').get()
            item['region'] = region_name
            yield scrapy.Request(response.urljoin(region_url), callback=self.parse_house_page, meta={"item":item})


    def parse_house_page(self, response):
        # 翻页
        item = response.meta.get('item')
        totalPage = response.css(".content__pg ::attr(data-totalpage)").get()
        for x in range(1, int(totalPage)):
            yield scrapy.Request(response.url + "pg" + str(x), callback=self.parse_house_list, meta={"item": item})


    def parse_house_list(self, response):
        # 解析房源列表
        item = response.meta.get("item")
        detail_urls = response.css('.content__list--item--main a::attr(href)').getall()
        for detail_url in detail_urls:
            # https://cs.lianjia.com/zufang/CS2311332725707251712.html
            # print(detail_url)
            result = re.search(r'/zufang/.+\d+\.html',detail_url)
            if result:
                detail_url = response.urljoin(detail_url)
                yield scrapy.Request(detail_url, callback=self.parse_house, meta={"item": item})


    def parse_house(self, response):
        # 解析房源详情页
        print(response.url)
        item = response.meta.get('item')
        item['title'] = response.css('.content__title ::text').get()
        price = response.css('.content__aside--title ::text').getall()
        item['price'] = ''.join(price).strip().replace('\n', "").replace(' ', "")
        info_list = response.css('.content__article__table span::text').getall()
        item['house_type'] = info_list[1]
        item['full_area'] = info_list[2]
        item['orientation'] = info_list[3]
        house_pushtime = response.css('.content__subtitle ::text').getall()[2]
        item['house_pushtime'] = house_pushtime.strip().replace(" ", "")
        base_info = response.css('.content__article__info ul li::text').getall()
        item['base_info'] = base_info[0] + " " + base_info[1] + " " + base_info[2] + "," + base_info[4] + "," + base_info[5] + "," + base_info[7] + "," + base_info[8] + "," + base_info[10] + "," + base_info[11] + "," + base_info[13] + "," + base_info[14] + "," + base_info[16]
        peitao = response.css('.content__article__info2 li::text').getall()
        item['peitao'] = ''.join(peitao).strip().replace('\n', "").replace(' ', "")
        house_information = response.css('.content__article__info3 p::text').getall()
        item['house_information'] = ''.join(house_information).strip().replace(" ", "")

        yield item



