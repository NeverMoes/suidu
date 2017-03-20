import scrapy
import json
from ..items import HackerNewsItem


class HackerNewsSpider(scrapy.Spider):
    name = 'hackernews'
    item_url_format = 'https://hacker-news.firebaseio.com/v0/item/{id}.json'

    def start_requests(self):
        yield scrapy.Request(
            url='https://hacker-news.firebaseio.com/v0/topstories.json',
            callback=self.parse_topstories
        )

    def parse_items(self, response):
        item = HackerNewsItem()
        jres = json.loads(response.text)

        item['url'] = jres['url']
        item['title'] = jres['title']
        item['id'] = jres['id']
        item['score'] = jres['score']
        item['time'] = jres['time']

        yield item

    def parse_topstories(self, response):
        jres = json.loads(response.text)
        for index in range(50):
            yield scrapy.Request(
                url=self.item_url_format.format(id=jres[index]),
                callback=self.parse_items
            )
