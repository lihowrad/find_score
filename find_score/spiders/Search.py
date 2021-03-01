# -*- coding: utf-8 -*-

import scrapy
import re
from datetime import datetime
from find_score.items import FindScoreItem
from scrapy.utils.project import get_project_settings


class Search(scrapy.Spider):
    settings = get_project_settings()
    name = 'Search'
    url = settings.get('URL')
    kv = {
        "User_Agent": settings.get("USER_AGENT")}

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.kv)

    def parse(self, response):
        item = FindScoreItem()
        results = re.findall('查询时间暂未开放', response.text, re.S)
        now = datetime.now()
        if not results:
            print('有新的内容更新!')
        else:
            print('查询时间暂未开放')
            item['remnant'] = '查询时间暂未开放'
        item['search_time'] = now.strftime("%Y--%m--%d %H:%M:%S")
        yield item
