# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapyofappItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class DoubanItem(Item):
    groupName = Field()
    groupURL = Field()
    totalNumber = Field()
    RelativeGroups = Field()
    ActiveUesrs = Field()