'''
Created on 2018年2月26日

@author: Administrator
'''


class UrlManager(object):
    
    def __init__(self):
        self.newUrls = set() #页面链接
        self.oldUrls = set() # 已爬取过的链接
        self.listUrls = set() # 列表的链接
        
    
    def addListUrl(self,url):
        if url is None:
            return
        self.listUrls.add(url)
        
        
    def addListUrls(self,urls):
        if urls is None and len(urls) == 0:
            return
        for url in urls:
            self.addListUrl(url)
        
    def addNewUrl(self,url):    #添加一条新链接
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)
    
    
    def addNewUrls(self,urls):  #添加多条新链接
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addNewUrl(url)
        
    
    def hasNewUrl(self): #判断是否存在未爬链接
        return len(self.newUrls) != 0
    
    def getNewUrl(self):
        newUrl = self.newUrls.pop() #取一条新链接
        self.oldUrls.add(newUrl)
        return newUrl

