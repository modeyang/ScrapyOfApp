#!/usr/bin/python
#coding=utf-8

"""MongoDB Pipeline for scrapy"""
import os, sys
project_path = os.path.dirname(__file__)
project_path = os.path.join(project_path, '..')
sys.path.append(project_path)

import pymongo
from scrapy import log

MONGODB_SAFE = False
MONGODB_ITEM_ID_FIELD = "_id"

class MongoDBPipeline(object):
    def __init__(self, mongodb_server, mongodb_port, mongodb_db, mongodb_collection, mongodb_uniq_key,
                 mongodb_item_id_field, mongodb_safe):
        connection = pymongo.Connection(mongodb_server, mongodb_port)
        self.mongodb_db = mongodb_db
        self.db = connection[mongodb_db]
        self.mongodb_collection = mongodb_collection
        self.collection = self.db[mongodb_collection]
        self.uniq_key = mongodb_uniq_key
        self.itemid = mongodb_item_id_field
        self.safe = mongodb_safe

        if isinstance(self.uniq_key, basestring) and self.uniq_key == "":
            self.uniq_key = None
            
        if self.uniq_key:
            self.collection.ensure_index(self.uniq_key, unique=True)


    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings.get('MONGODB_SERVER', 'localhost'), settings.get('MONGODB_PORT', 27017),
                   settings.get('MONGODB_DB', 'scrapy'), settings.get('MONGODB_COLLECTION', None),
                   settings.get('MONGODB_UNIQ_KEY', None), settings.get('MONGODB_ITEM_ID_FIELD', MONGODB_ITEM_ID_FIELD),
                   settings.get('MONGODB_SAFE', MONGODB_SAFE))


    def process_item(self, item, spider):
        if self.uniq_key is None:
            result = self.collection.insert(dict(item), safe=self.safe)
        else:
            result = self.collection.update({ self.uniq_key: item[self.uniq_key] }, { '$set': dict(item) },
                                            upsert=True, safe=self.safe)

        # If item has _id field and is None
        if self.itemid in item.fields and not item.get(self.itemid, None):
            item[self.itemid] = result

        log.msg("Item %s wrote to MongoDB database %s/%s" % (result, self.mongodb_db, self.mongodb_collection),
                level=log.DEBUG, spider=spider)
        return item