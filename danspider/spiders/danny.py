# -*- coding: utf-8 -*-
import scrapy


class DannySpider(scrapy.Spider):
    name = 'danny'
    allowed_domains = ['jiji.com.ng']
    start_urls = ['http://jiji.com.ng/']

    def parse(self, response):
        pass
