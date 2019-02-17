# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor
from dazhongdp.items import DazhongdpItem
import cssutils
from xml.dom.minidom import parseString
import re


class DpinfoSpider(CrawlSpider):
    name = 'dpinfo'
    allowed_domains = ['www.dianping.com','s3plus.meituan.net']

    search_word = u'可颂坊'
    base_url = 'https://www.dianping.com/search/keyword/7/10_'+ search_word
    start_urls = [base_url]

    exShop = LinkExtractor(allow=(r'http://www.dianping.com/shop/\d+'),
                           restrict_xpaths=('//div[@class="tit"]/a'))

    page_url = base_url + r'/p\d+'
    exPage = LinkExtractor(restrict_xpaths=('//div[@class="page"]/a[@class="next"]'))

   
    rules = [
        Rule(exShop,callback='parse_shop',follow=False),
        #Rule(exPage,follow=True),
        ]

        

    def parse_shop(self,response):
        item  = DazhongdpItem()

        item['decrypt_css'] = 'http:' + response.xpath('//link[@rel="stylesheet"]/@href').extract()[1]
        

        item['shop_name'] = response.xpath('//h1[@class="shop-name"]/text()').extract_first()
        item['shop_addr'] = response.xpath('//span[@id="address"]/*/@class | //span[@id="address"]/text()  ').extract()
        
        brief_info = response.xpath('//div[@class="brief-info"]')
        item['rank'] = brief_info.xpath('//span/@title').extract_first()
        item['reviewCount'] = brief_info.xpath('//span[@id="reviewCount"]/d/@class | //span[@id="reviewCount"]/text()').extract()
        item['avgPrice'] = brief_info.xpath('//span[@id="avgPriceTitle"]/d/@class | //span[@id="avgPriceTitle"]/text()').extract()
        
        item['comm_env'] =  brief_info.xpath('//span[@id="comment_score"]/span[2]/d/@class | //span[@id="comment_score"]/span[2]/text()').extract()
        item['comm_taste'] =  brief_info.xpath('//span[@id="comment_score"]/span[1]/d/@class | //span[@id="comment_score"]/span[1]/text()').extract()
        item['comm_serve'] =  brief_info.xpath('//span[@id="comment_score"]/span[3]/d/@class | //span[@id="comment_score"]/span[3]/text()').extract()

        item['dmap'] = {}
        req =  scrapy.Request(item['decrypt_css'],callback=self.parse_css,dont_filter=True)
        req.meta['item'] = item

        yield req

    def parse_css(self,response):
        item = response.meta['item']
        sheet = cssutils.parseString(response.body)
        svgurl = {}
        g ={}
        reqs = []
        for rule in sheet:
             for p in rule.style:
                if p.name == 'background-image':
                    key = re.match(r'\w+\[class.{2}"(\w+)"\]',rule.selectorText).group(1)
                    svgurl[key]='http:'+ p.value[4:-1]
                    req = scrapy.Request(svgurl[key],callback=self.parse_svg,dont_filter=True)
                    req.meta['svgname'] = key
                    reqs.append(req)
                if p.name == 'background':
                    xy = re.match(r'\D*(\d+)\D*(\d+)\D*',p.value)
                    try:
                        g[rule.selectorText[1:]] = [xy.group(1),xy.group(2)]
                    except AttributeError:
                        pass
        item['xys'] = g
        for req in reqs:
            req.meta['item'] = item
            yield req


    def parse_svg(self,response):
        item = response.meta['item']
        pre_ys = response.xpath("//@y  | //@d").extract()
        ys = []
        
        for y in pre_ys:
            tmp = re.match(r'M\d (\d+) H\d+',y)
            if tmp:
                ys.append(tmp.group(1))
            else:
                ys.append(y)
        
        doc = parseString(response.body)
        root = doc.documentElement
        tp = root.getElementsByTagName('textPath')
        sp = root.getElementsByTagName('text')
        true_d = None
        decode = []

        if len(tp) == len(ys):
            true_d = tp
        elif len(sp) == len(ys):
            true_d = sp

        for d in true_d:
            decode.append(d.childNodes[0].data)           
       
        item['dmap'][response.meta['svgname']] =  dict(zip(ys,decode))
        yield item






