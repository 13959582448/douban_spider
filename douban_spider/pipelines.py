# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanSpiderPipeline(object):
    def __init__(self):
        self.file=open(r"/home/huangchenhan/data.txt","w",encoding="utf-8")
        self.word=open(r"/home/huangchenhan/word.txt","w",encoding="utf-8")
        self.users=open(r"/home/huangchenhan/user.txt","w",encoding="utf-8")
    def process_item(self, item, spider):
        json.dump(dict(item),fp=self.file,ensure_ascii=False)
        self.word.write(item["title"]+"\n")
        self.users.write(item["author"]+"\n")
        self.file.write("\n")
        return item
