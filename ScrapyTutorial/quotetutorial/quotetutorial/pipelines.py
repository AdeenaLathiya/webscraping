# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped Data -> Item Containers -> JSON/CSV files
# Scraped Data -> Item Containers -> Pipeline -> SQL/MongoDB database

import pymongo
from pymongo import database


class QuotetutorialPipeline(object):

    def __init__(self):
        # Create conection
        self.conn = pymongo.MongoClient('localhost', 27017)

        # Create database
        db =  self.conn['myquotes']

        # Create table
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        # print("Pipeline: " + item['title'][0])
        self.collection.insert(dict(item))
        return item
