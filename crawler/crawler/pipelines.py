import pymongo
import datetime
import time

class MongodbPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.suidu

    # @classmethod
    # def from_crawler(cls, crawler):
    #     pass
    #
    # def open_spider(self, crawler):
    #     self.client = pymongo.mongoclient()
    #     self.db = self.client.suidu
    #     return
    #
    # def close_spider(self, crawler):
    #     self.client.close()
    #     return

    def process_item(self, item, spider):
        col = self.db[spider.name]

        today = datetime.date.today()
        date = datetime.datetime(today.year, today.month, today.day)

        data = dict(item)
        data['date'] = date

        col.insert_one(data)
        return item
