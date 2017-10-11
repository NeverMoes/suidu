import scrapy
from ..items import GithubTrendingItem
from bs4 import BeautifulSoup

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
        response_test = response.text
        result = BeautifulSoup(response_test,'lxml')
        for sel in result.select('div.explore-content > ol > li'):
            href = sel.find("a")['href']
            item['url'] = self.url_prefix+"/"+href
            item['desc'] = sel.find("p").text
            item['owner'] = href.split("/")[1]
            item['repo'] = href.split("/")[2]
            try:
                item['type'] = sel.select('span[itemprop="programmingLanguage"]')[0].text
            except:
                item['type'] = None
            item['stars'] = sel.select('svg[aria-label="star"]')[0].parent.text.strip()
            item['forks'] = sel.select('svg[aria-label="fork"]')[0].parent.text.strip()
            item['today_stars'] = sel.select('svg[aria-hidden="true"]')[1].parent.text.strip()
            yield item