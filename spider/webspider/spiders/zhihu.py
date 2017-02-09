import scrapy
from . import universal

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/']

    def __init__(self):
        super().__init__()
