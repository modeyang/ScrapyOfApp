#!/usr/bin/python
#coding=utf-8
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class ScrapyofappPipeline(object):
    def __init__(self):
        self.f = open('save.out', 'w')
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
        
    def process_item(self, item, spider):
        self.f.write(('%s\n' % item).encode('utf-8'))
        return item

    def initialize(self):
        pass
    
    def finalize(self):
        self.f.close()