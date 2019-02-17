# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import os
import shutil

class BaiduimgPipeline(ImagesPipeline):
    img_store = get_project_settings().get('IMAGES_STORE')+"\\"

    def get_media_requests(self, item, info):
        for url in item['img_url']:
            yield Request(url,meta={'name':item['name']})

    def item_completed(self, results, item, info):
        img_paths = [x['path'] for ok, x in results if ok]
        if not img_paths:
            raise DropItem("No images.")
        newdir = self.img_store + item["name"]
        if not os.path.exists(newdir):
            os.mkdir(newdir)

        newname = newdir +"\\"+item['num'] + '.jpg'
        oldname = self.img_store +img_paths[0]
        shutil.move(oldname,newname)
        return item
    
