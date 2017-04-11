#!/usr/bin/python35
#-*- coding:utf-8 –*-


import json
import os
import sys
import time

import pymongo
import requests
from pyquery import PyQuery as pq


class SpiderClient:
    def __init__(self, HOST="localhost", PORT=27017, DB="jd"):
        self.connection = pymongo.MongoClient(HOST, PORT)
        self.db = DB
    
    def run(self):
        r = requests.get('https://www.lagou.com/')
        cookies = r.cookies.get_dict()
        print(cookies)
        url = 'https://www.lagou.com/jobs/positionAjax.json?gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&px=default&yx=10k-15k&gx=%E5%85%A8%E8%81%8C&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
        result = requests.post( url, data = { 'first':True, 'pn':1, 'kd':'前端开发'}, cookies = cookies )
        jq = pq(result.text)
        print(jq)
        v = jq('a.position_link')
        print( jq('.position_link') )
        pass

if __name__ == '__main__':
    spider = SpiderClient()
    spider.run()
