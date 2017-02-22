import scrapy
import requests
from scrapy.contrib.loader import ItemLoader

url = 'https://github.com/trending?since=daily'

url_prefix = 'https://github.com'

req = requests.get(url)

response = scrapy.http.HtmlResponse()

sel = scrapy.selector.Selector(text=req.text)

for s in sel.css('div.explore-content > ol > li'):
    divs = s.css('div')
    url = divs[0].css('h3 > a::attr(href)').extract_first()
    _, owner, repo = url.split('/')
    url = url_prefix + url
    desc = divs[2].css('p::text').extract_first().strip()
    stars = divs[3].css('a[aria-label="Stargazers"]::text').extract()[1].strip()
    forks = divs[3].css('a[aria-label="Forks"]::text').extract()[1].strip()
    today = divs[3].css('span.float-right::text').extract()[1].strip()

    type = divs[3].css('span[itemprop="programmingLanguage"]::text').extract_first().strip()

    if not type:
        type = 'None'

    print(owner)
    print(repo)
    print(url)
    print(desc)
    print(stars)
    print(forks)
    print(today)
    print(type)

    print('---------------------')
