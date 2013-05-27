#!/usr/bin/python
#coding=utf-8

from scrapy.spider import BaseSpider
from scrapy.item import item
from ScrapyOfApp.items import DoubanItem

class GroupSpider(BaseSpider):
	name = 'douban'
	allowed_domains = ["douban.com"]
	start_urls = [
		# "http://www.douban.com/group/",
		"http://www.douban.com/group/explore?tag=%E7%94%9F%E6%B4%BB",
	]

	rules = (
		Rule (SgmlLinkExtractor(allow=('/group/[^/]+/$',)), callback="parse_items", process_request='add_cookie'),
		Rule (SgmlLinkExtractor(allow=('/group/explore\?tag', )), follow=True, process_request='add_cookie'), 
    )

	def add_cookie(self, request):
		request.replace(cookies=[
			{'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'}, 
			])
		return request

	def parse_items(self, response):
		self.log("Fetch douban homepage page: %s" % response.url)
		open("test.data", "wb").write(response.body)

		# le = SgmlLinkExtractor(allow=r'/ad/[^/]+/67-\d+\.html')
		# le.extract_links(response)
		return None