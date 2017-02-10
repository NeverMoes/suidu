import os
import sys
sys.path.insert(0, os.path.abspath('..'))


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spider.webspider.spiders.douban import DoubanSpider

# suidu/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)
# 指定要启动的爬虫
process.crawl(DoubanSpider)
# 启动爬虫，会阻塞，直到爬取完成
process.start()