# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapyofappItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class DoubanItem(Item):
    # define the fields for your item here like:
    # name = Field()
    groupName = Field()
    groupURL = Field()
    totalNumber = Field()
    RelativeGroups = Field()
    ActiveUesrs = Field()