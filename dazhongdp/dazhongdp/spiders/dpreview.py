# -*- coding: utf-8 -*-
import scrapy


class DpreviewSpider(scrapy.Spider):
    name = 'dpreview'
    allowed_domains = ['www.dianping.com']
    start_urls = ['http://www.dianping.com/']

    def parse(self, response):
        pass
