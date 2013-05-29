# Scrapy settings for ScrapyOfApp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os
project_path = os.path.dirname(__file__)

BOT_NAME = 'ScrapyOfApp'

SPIDER_MODULES = ['ScrapyOfApp.spiders']
NEWSPIDER_MODULE = 'ScrapyOfApp.spiders'

ITEM_PIPELINES = [
  'ScrapyOfApp.pipelines.ScrapyofappPipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyOfApp (+http://www.yourdomain.com)'

# mogodb pipeline
# ITEM_PIPELINES = [
#   'scrapymongodb.MongoDBPipeline',
# ]

# MONGODB_SERVER = 'localhost'
# MONGODB_PORT = 27017
# MONGODB_DB = 'scrapy'
# MONGODB_COLLECTION = 'items'
# MONGODB_UNIQ_KEY = 'url'
# MONGODB_ITEM_ID_FIELD = '_id'
# MONGODB_SAFE = True

# # redis scrapy
# # enables scheduling storing requests queue in redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# # don't cleanup redis queues, allows to pause/resume crawls
# SCHEDULER_PERSIST = True

# # Schedule requests using a priority queue. (default)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# # Schedule requests using a queue (FIFO).
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# # Schedule requests using a stack (LIFO).
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# # Max idle time to prevent the spider from being closed when distributed crawling
# # this only work if queue class is SpiderQueue or SpiderStack
# # and may also block the same time when your spider start at the first time (because the queue is empty).
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# ITEM_PIPELINES += [
# 	'scrapy_redis.pipelines.RedisPipeline',
# ]