import scrapy
from ..items import GithubTrendingItem


class GithubTrendingSpider(scrapy.Spider):
    name = 'github_trending'
    allowed_domains = ['github.com']
    url_prefix = 'https://github.com'

    def start_requests(self):
        urls = [
            'https://github.com/trending',
        ]

        yield scrapy.Request(
            url = 'https://github.com/trending',
            callback=self.parse_trending()
        )

    def parse_trending(self, response):
        item = GithubTrendingItem()

        for sel in response.css('div.explore-content > ol > li'):
            divs = sel.css('div')
            url = divs[0].css('h3 > a::attr(href)').extract_first()
            _, owner, repo = url.split('/')

            item['url'] = self.url_prefix + url
            item['desc'] = divs[2].css('p::text').extract_first().strip()
            item['stars'] = divs[3].css('a[aria-label="Stargazers"]::text').extract()[1].strip()
            item['forks'] = divs[3].css('a[aria-label="Forks"]::text').extract()[1].strip()
            item['today_stars'] = divs[3].css('span.float-right::text').extract()[1].strip()

            type = divs[3].css('span[itemprop="programmingLanguage"]::text').extract_first().strip()
            if not type:
                type = 'None'

            item['type'] = type
            yield item



