# -*- coding: utf-8 -*-
import scrapy
from dazhongdp.spiders.dpinfo import DpinfoSpider
from scrapy.linkextractors import LinkExtractor
from dazhongdp.items import DazhongReviewItem
from scrapy.spiders import Rule

class DpreviewSpider(DpinfoSpider):
    name = 'dpreview'
    allowed_domains = DpinfoSpider.allowed_domains
    #start_urls = [DpinfoSpider.base_url]
    start_urls = ['https://www.dianping.com/search/keyword/7/10_子情贝诺']


    exReview = LinkExtractor(allow=(r'/shop/\d+/review_all/p\d+'),
                            restrict_xpaths=('//div[@class="reviews-pages"]/a[@class="NextPage"]'))
    

    rules = DpinfoSpider.rules
    rules.append(Rule(exReview,callback='parse_review',follow=True))

    def parse_shop(self, response):
        review_all = response.url + '#comment'
        req = scrapy.Request(review_all,callback=self.parse_review,dont_filter=True)
        yield req
    


    def parse_review(self,response):
        item = DazhongReviewItem()
        item['decrypt_css'] = 'http:' + response.xpath('//link[@rel="stylesheet"]/@href').extract()[1]
        item['shop_name'] = response.xpath('//h1[@class="shop-name"]/text()').extract_first()

        item['review_list'] = []
        #review_list = response.xpath('//div[@class="review-words Hide"] | //div[@class="review-words"]')
        review_list = response.xpath('//div[@class="info J-info-all clearfix Hide"]/p | //div[@class="content"]/p[@class="desc"]')
        for review in review_list:
            item['review_list'].append(review.xpath('b/@class | span/@class | text()').extract())
        
        
        item['dmap'] = {}
        req = scrapy.Request(item['decrypt_css'],callback=self.parse_css,dont_filter=True)
        req.meta['item'] = item

        yield req


        
        

