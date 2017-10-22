import scrapy
from scrapy.contrib.spiders import XMLFeedSpider
from ..items import juejinItem

class JuejinRssSpider(XMLFeedSpider):
    name = "juejin"
    start_urls = ['https://juejin.im/rss']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response,node):
        item = juejinItem()

        node.remove_namespaces()

        item['title'] = node.xpath('title/text()').extract()
        item['desc'] = node.xpath('description/text()').extract()
        item['url'] = node.xpath('link/text()').extract()
        item['category'] = node.xpath('category/text()').extract()[0]
        item['writer'] = node.xpath("creator/text()").extract()
        item['data'] = node.xpath('pubDate/text()').extract()

        return item