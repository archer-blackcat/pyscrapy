# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DazhongdpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    shop_name = scrapy.Field()
    shop_addr = scrapy.Field()
    
    rank = scrapy.Field()
    
    reviewCount = scrapy.Field()
    avgPrice = scrapy.Field()

    comm_env = scrapy.Field()
    comm_taste = scrapy.Field()
    comm_serve = scrapy.Field()

    decrypt_css = scrapy.Field()
    decrypt_svg = scrapy.Field()

    xys = scrapy.Field()
    dmap = scrapy.Field()

    pass

class DazhongReviewItem(scrapy.Item):

    shop_name = scrapy.Field()

    review_list = scrapy.Field()

    decrypt_css = scrapy.Field()
    decrypt_svg = scrapy.Field()

    xys = scrapy.Field()
    dmap = scrapy.Field()
    pass

