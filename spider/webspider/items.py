# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    rating_people = scrapy.Field()
    # tags = scrapy.Field()


class WebspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
