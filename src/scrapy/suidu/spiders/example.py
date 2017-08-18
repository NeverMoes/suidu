# -*- coding: utf-8 -*-

# spider for test using

import scrapy
from pymongo import MongoClient
import os



class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
    )

    def parse(self, response):
        try:
            mongo_url = os.environ.get("MONGODB_PORT_27017_TCP_ADDR") + ":" + os.environ.get("MONGODB_PORT_27017_TCP_PORT")
        except:
            print("env err")
        text = response.css('h1::text').extract_first()
        client = MongoClient(mongo_url)
        db = client.test
        col = db.test
        col.insert_one({"text": text})

