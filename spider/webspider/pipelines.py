import pymongo


class DoubanBookPipeline(object):
    pass


class MongodbPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        pass

    def open_spider(self, spider):
        self.client = pymongo.MongoClient()
        self.db = self.client.test
        self.col = self.db.github
        return

    def close_spider(self, spider):
        self.client.close()
        return

    def process_item(self, item, spider):
        client = pymongo.MongoClient()
        db = client.test
        col = db.github
        col.insert_one({'name': 'test'})



