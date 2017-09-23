#!/usr/bin/env bash

docker build -t suidu:django ./django/
docker build -t suidu:mongodb ./mongodb/
docker build -t suidu:nginx ./nginx/
docker build -t suidu:scrapy ./scrapy/
docker build -t suidu:scrapyd ./scrapyd/
docker build -t suidu:vue ./vue/

