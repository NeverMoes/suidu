# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class SuiduPipeline(object):
    def process_item(self, item, spider):
        return item

import pymongo
import datetime
import time

class MongodbPipeline(object):

    def process_item(self, item, spider):
        mongo_url = os.environ.get("MONGODB_PORT_27017_TCP_ADDR") + ":" + os.environ.get("MONGODB_PORT_27017_TCP_PORT")
        client = pymongo.MongoClient(mongo_url)
        db = client.suidu
        col = db[spider.name]

        col.insert_one(dict(item))

        return item
