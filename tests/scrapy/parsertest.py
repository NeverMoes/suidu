import scrapy
import requests
import json


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

req = requests.get(url)

js = json.loads(req.text)

print(js)

print(type(js))