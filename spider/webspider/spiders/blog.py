import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_url = 'http://mindhacks.cn/page/1/'