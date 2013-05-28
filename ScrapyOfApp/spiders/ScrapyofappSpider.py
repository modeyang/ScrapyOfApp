#!/usr/bin/python
#coding=utf-8
import os, sys
project_path = os.path.abspath(__file__)
project_path = project_path[:project_path.rfind('ScrapyOfApp')]
sys.path.append(project_path)

from scrapy.spider import BaseSpider
from ScrapyOfApp.items import ScrapyofappItem

class  AppSpider(BaseSpider):
	name = "360doc.com"
	start_urls = [
		"http://www.360doc.com/content/09/0628/22/88761_4065911.shtml",
	]		

	def parse(self, response):
		filename = response.url.split("/")[-2]
		print 'filename : ' + filename