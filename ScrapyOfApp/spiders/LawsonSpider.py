#!/usr/bin/python
#coding=utf-8

'''
Created on 2013-5-29

@author: computer
'''
import os, sys
project_path = os.path.abspath(__file__)
project_path = project_path[:project_path.rfind('ScrapyOfApp')]
sys.path.append(project_path)

from urlparse import urljoin

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.response import get_base_url
# debug
from scrapy.shell import inspect_response

from ScrapyOfApp.items import ConvStore

class StoreLoader(XPathItemLoader):
    default_output_processor = Compose(lambda v: v[0], unicode.strip)

    def branch_in(self, values):
        for v in values:
            v = v.strip()
            yield v + u'店' if not v.endswith(u'店') else v
            
            
class LawsonSpider(CrawlSpider):
    name = 'lawson'
    start_urls = ['http://www.lawson.com.cn/shops']
    allowed_domains = ['lawson.com.cn']
    rules = (
            Rule(SgmlLinkExtractor(allow=r'list\?area_id=\d+', tags='a'),
                callback='parse_store_list'),
            )

    def parse_geo(self, response):
#         inspect_response(response)
        hxs = HtmlXPathSelector(response)
        store = response.meta['store']

        lng, lat = hxs.re(r'(\d+\.\d+),(\d+\.\d+)')
        store.add_value('latitude', lat)
        store.add_value('longitude', lng)
        return store.load_item()

    def parse_store_list(self, response):
        hxs = HtmlXPathSelector(response)
        store_selectors = hxs.select('//div[@class="ShopList"]/table/tr')[1:]
        
#         items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls]) 

        for s in store_selectors:
            store = StoreLoader(item=ConvStore(), response=response)
            store.add_value('name', u'罗森')
            store.add_value('alias', u'Lawson')
            store.add_value('branch', s.select('th/p/text()').extract())
            store.add_value('address', s.select('td/span/text()').extract())
            store.add_value('district', response.meta['link_text'])
            store.add_value('city', u'上海')

            map_rel_url = s.select('td/a/@rel').extract()
            if map_rel_url:
                map_url = urljoin(get_base_url(response), map_rel_url[0])
                req = Request(map_url, callback=self.parse_geo)
                req.meta['store'] = store
                yield req
            else:
                yield store.load_item()