import scrapy
from ..items import GithubTrendingItem


class GithubTrendingSpider(scrapy.Spider):
    name = 'github_trending'
    url_prefix = 'https://github.com'

    def start_requests(self):
        yield scrapy.Request(
            url='https://github.com/trending',
            callback=self.parse_trending
        )

    def parse_trending(self, response):
        item = GithubTrendingItem()
        for sel in response.css('div.explore-content > ol > li'):
            divs = sel.css('div')
            url = divs[0].css('h3 > a::attr(href)').extract_first()
            _ ,item['owner'] ,item['repo'] = url.split('/')
            item['url'] = self.url_prefix + url
            desc = divs[2].css('p::text').extract_first()
            item['desc'] = desc.strip() if desc else None
            item['stars'] = divs[3].css('a[class="muted-link d-inline-block mr-3"]::text').extract()[1].strip()
            item['forks'] = divs[3].css('a[class="muted-link d-inline-block mr-3"]::text').extract()[3].strip()
            item['today_stars'] = divs[3].css('span[class="d-inline-block float-sm-right"]::text').extract()[1].strip()
            type = divs[3].css('span[itemprop="programmingLanguage"]::text').extract_first()
            item['type'] = type.strip() if type else None
            yield item