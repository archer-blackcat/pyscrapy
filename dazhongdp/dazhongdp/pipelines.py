# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import os
import os.path

class DazhongdpPipeline(object):

    def process_item(self, item, spider):
        filename = 'C:\\Users\\Tetrarrow\\Documents\\Scrapped\\dzdp\\' + item['shop_name'] + '.txt'
        f = open(filename,'w')
        lines = []

        xys = item['xys']
        dmap = item['dmap']

        f.write(item['shop_name']+'\n')
        f.write(item['rank']+'\n')
        f.write(self.decode(item['shop_addr'],xys,dmap)+'\n')
        f.write(self.decode(item['avgPrice'],xys,dmap)+'\n')
        f.write(self.decode(item['reviewCount'],xys,dmap)+'\n')
        f.write(self.decode(item['comm_taste'],xys,dmap)+'\n')
        f.write(self.decode(item['comm_env'],xys,dmap)+'\n')
        f.write(self.decode(item['comm_serve'],xys,dmap)+'\n')

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
                            dm = list(filter(lambda v: int(v)>y,dmap[m].keys()))
                            dm = sorted(dm)                     
                            result.append(dmap[m][dm[0]][x])
                except KeyError:
                    result.append(s)
        return ''.join(result)
                    