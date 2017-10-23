''''
A simple tool to get top app list from Google Play (https://play.google.com/store/apps/)
'''
#!/usr/bin/python

import os
import urllib.parse as urllib
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from bs4 import BeautifulSoup
from Utils import PackageInfo, GooglePalyConstants as CONSTANT

class TopAppListCrawler:
    category = CONSTANT.CATEGORY_GAME
    collection = CONSTANT.COLLECTION_TOPGROSSING
    def __init__(self, category, collection):
        self.category = category
        self.collection = collection

    def getList(self):
        url = CONSTANT.url(self.category, self.collection)
        print('gat app list from: '+url)
        values = {'start' : 0,
                  'num' : 100,
                  'numChildren' : 0,
                  'ipf' : 1,
                  'xhr' : 1}
        data = urllib.urlencode(values)
        data = data.encode('utf-8')
        req = urllib2.urlopen(
            urllib2.Request(url, data)
        )
        soup = BeautifulSoup(req.read().decode('utf-8'), 'html.parser')
        packages = soup.find_all("a",class_="title")
        apps = []
        for pkg in packages:
            pkgName = pkg.get('href').split("=")[1]
            pkgLabel = pkg.get('title')
            info = PackageInfo(pkgName, pkgLabel)
            apps.append(info)
        return apps

if __name__ == '__main__':
    cats = [CONSTANT.CATEGORY_GAME, CONSTANT.CATEGORY_COMMUNICATION, CONSTANT.CATEGORY_SOCIAL]
    collections = [CONSTANT.COLLECTION_TOPSELLING_FREE, CONSTANT.COLLECTION_TOPSELLING_PAID, CONSTANT.COLLECTION_TOPGROSSING]
    for cat in cats:
        for collection in collections:
            print(" ----- ")
            crawler = TopAppListCrawler(cat, collection)
            appList = crawler.getList()
            i = 0
            for app in appList:
                i = i+1
                print(str(i)+". package info:"+app.packageName+" | "+app.label)
    print("\nDONE!")
