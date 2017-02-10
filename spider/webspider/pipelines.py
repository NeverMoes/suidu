# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymango


class DoubanBookPipeline(object):
    pass


class MongodbPipeline(object):
    collection_name = 'douban_cartoon' # mongo的collection相当于sql的table

    def __init__(self, mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    ## 配置mongo
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'), #从settings中mongo的uri
            mongo_db=crawler.settings.get('MONGO_DATABASE','douban') #从settings中获取数据库，默认为douban
        )

    # 在spider工作开始前连接mongodb
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    ## 在spider工作结束后关闭连接
    def close_spider(self, spider):
        self.client.close()
    ## 在mongodb中插入数据
    def process_item(self, item, spider):
        # for i in item:

        self.db[self.collection_name].insert(dict(item))
        return item




class WebspiderPipeline(object):
    def process_item(self, item, spider):
        return item
