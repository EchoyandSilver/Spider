# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://www.httpbin.org/user-agent']

    def parse(self, response):
        print(response.text)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
