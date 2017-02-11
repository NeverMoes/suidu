import scrapy
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoubanBookItem
import random
import string


class DoubanSpider(scrapy.Spider):
    """
    豆瓣读书爬虫
    """
    name = 'douban'

    def start_requests(self):
        url_format = 'https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6?start={num}&type=T'
        bid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
        for num in range(0, 1000, 20):
            yield scrapy.Request(
                url=url_format.format(num=num),
                callback=self.parse_page,
                cookies={'bid': bid}
            )

    def parse_page(self, response):
        item = DoubanBookItem()
        for sel in response.css('#subject_list > ul > li > div.info'):
            item['title']= sel.css('h2 > a::text').extract_first()
            item['link'] = sel.css('h2 > a::attr(href)').extract_first()
            item['rating'] = sel.css('div.star.clearfix > span.rating_nums::text').extract_first()
            item['rating_people'] = sel.css('div.star.clearfix > span.pl::text').extract_first()
            print(item)
            # yield item

    def parse_book(self, response):
        pass


