# -*- coding: utf-8 -*-
import scrapy
import urllib.parse as P
import json
from baiduimg.items import BaiduimgItem



class BdimgSpider(scrapy.Spider):
    name = 'bdimg'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        } 
    allowed_domains = ['image.baidu.com']
    #start_urls = ['http://image.baidu.com/']
   
    

    def __init__(self, target = '美女',quant = 1200, **kwargs):
        super().__init__(**kwargs)
        self.target_name = target
        self.target_quantity = quant


    def start_requests(self):
        pn = int(self.target_quantity/30)
        q = {
            'tn': ['resultjson_com'],
            'ipn': ['rj'],
            'fp': ['result'], 
            'queryWord': [self.target_name],
            'cl': ['2'],
            'lm': ['-1'],
            'ie': ['utf-8'], 
            'oe': ['utf-8'], 
            'st': ['-1'], 
            'ic': ['0'], 
            'word': [self.target_name], 'face': ['0'],'istype': ['2'], 'nc': ['1'], 'pn': ['0'], 'rn': ['30'], 'gsm': ['1e']
            }
        for i in range(pn):
            q['pn'] = [str(30 * i)]
            url = "https://image.baidu.com/search/acjson?" + P.urlencode(q,doseq=True)
            yield scrapy.Request(url,callback = self.parse,headers = self.headers)

    def parse(self, response):
         imgs = json.loads(response.body)['data']
         for img in imgs:
            item = BaiduimgItem()
            try:
                self.target_quantity -= 1
                item['name'] = self.target_name
                item['num'] = str(self.target_quantity)
                item['img_url'] = [img['middleURL']]
                yield item
            except Exception as e:
                print("Done Parsing %s imgs.\n" % (QUANTITY - self.target_quantity ))
