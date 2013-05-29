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
    
class ConvStore(Item):
    name = Field()
    branch = Field()
    alias = Field()
    address = Field()
    city = Field()
    district = Field()
    longitude = Field(serializer=float)
    latitude = Field(serializer=float)
    
    def __str__(self, *args, **kwargs):
        return Item.__str__(self, *args, **kwargs)


from os import path
print path.dirname(path.abspath(__file__))