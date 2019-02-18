# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import os
import os.path
import codecs
from dazhongdp.items import *

class DazhongdpPipeline(object):

    def process_item(self, item, spider):
        filename = 'C:\\Users\\asus\\Documents\\Scrapped\\dzdp\\' + item['shop_name'] + '.txt'
        xys = item['xys']
        dmap = item['dmap']

        
        if isinstance(item,DazhongdpItem):
            f = codecs.open(filename,'w',encoding='utf-8')
            f.write(item['shop_name']+'\n')
            f.write(item['rank']+'\n')
            f.write(self.decode(item['shop_addr'],xys,dmap)+'\r\n')
            f.write(self.decode(item['avgPrice'],xys,dmap)+'\r\n')
            f.write(self.decode(item['reviewCount'],xys,dmap)+'\r\n')
            f.write(self.decode(item['comm_taste'],xys,dmap)+'\r\n')
            f.write(self.decode(item['comm_env'],xys,dmap)+'\r\n')
            f.write(self.decode(item['comm_serve'],xys,dmap)+'\r\n')
        elif isinstance(item,DazhongReviewItem):
            f = codecs.open(filename,'w',encoding='utf-8')
            f.write(item['shop_name']+'\r\n')
            for reveiw in item['review_list']:
                f.write('==============\r\n')
                f.write(self.decode(reveiw,xys,dmap)+ '\r\n')

        f.close()
        print('============================Done'+ item['shop_name'] + '==================\n')

    def decode(self,strs,xys,dmap):
        matcher = re.compile(r'[a-z0-9]+$')
        result = []
        for s in strs:
            if not re.match(matcher,s):
                result.append(s)
            else:
                try:
                    x = int(int(xys[s][0])/14)
                    y = int(xys[s][1])
                    for m in dmap.keys():
                        if m == s[:len(m)]:
                            dm = list(filter(lambda v: int(v)>=y,dmap[m].keys()))
                            dm = sorted(dm,key=lambda v : int(v))                     
                            result.append(dmap[m][dm[0]][x])
                except KeyError:
                    result.append(s)
        return ''.join(result)
                    