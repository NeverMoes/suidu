# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.contrib.loader import ItemLoader


class DoubanBookItem(Item):
    url = Field()
    title = Field()
    rating = Field()
    rating_people = Field()
    # tags = Field()


class GithubTrendingItem(Item):
    url = Field()
    repo = Field()
    desc = Field()
    type = Field()
    stars = Field()
    today_stars = Field()
    owner = Field()
    forks = Field()



