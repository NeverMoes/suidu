import scrapy
from ..items import GithubTrendingItem


class GithubTrendingSpider(scrapy.Spider):
    name = 'github_trending'
    allowed_domains = ['github.com']
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
            _, owner, repo = url.split('/')

            item['url'] = self.url_prefix + url
            desc = divs[2].css('p::text').extract_first()
            item['desc'] = desc.strip() if desc else None
            item['stars'] = divs[3].css('a[aria-label="Stargazers"]::text').extract()[1].strip()
            item['forks'] = divs[3].css('a[aria-label="Forks"]::text').extract()[1].strip()
            item['today_stars'] = divs[3].css('span.float-right::text').extract()[1].strip()
            type = divs[3].css('span[itemprop="programmingLanguage"]::text').extract_first()
            item['type'] = type.strip() if type else None

            yield item



