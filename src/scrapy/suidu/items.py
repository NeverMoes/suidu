# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class SuiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GithubTrendingItem(Item):
    # 链接
    url = Field()
    # 仓库名
    repo = Field()
    # 项目描述
    desc = Field()
    # 语言类型
    type = Field()
    # star数
    stars = Field()
    # 今日star数
    today_stars = Field()
    # 所有者
    owner = Field()
    # fork数
    forks = Field()


class HackerNewsItem(Item):
    url = Field()
    id = Field()
    title = Field()
    time = Field()
    score = Field()