#!/usr/bin/python
#coding=utf-8
import os, sys
project_path = os.path.dirname(__file__)
project_path = os.path.join(project_path, '..')
sys.path.append(project_path)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from scrapy.conf import settings

# from scraping.items import AlchemyBase
from ScrapyOfApp.SqlAlchemyItems import AlchemyBase

class SQLAlchemyPipeline(object):
    def __init__(self):
        engine = create_engine(settings['SQLALCHEMY_ENGINE_URL'])
        AlchemyBase.metadata.bind = engine
        self.session = scoped_session(sessionmaker(engine))()
        # TODO: Don't drop all. Find a way to update existing entries.
        AlchemyBase.metadata.drop_all()
        AlchemyBase.metadata.create_all()


    def process_item(self, item, spider):
        if isinstance(item, AlchemyBase):
            self.session.add(item)
            try:
                self.session.commit()
            except SQLAlchemyError, e:
                self.session.rollback()
                raise e

        return item