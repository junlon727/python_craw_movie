'''
Created on 2018年2月26日

@author: Administrator
'''
from movie_spider import url_manager, html_downloader, html_parser,\
    html_outputer
from test.libregrtest.runtest import FAILED


class SpideMain(object):
    def __init__(self): #初始化(构造方法)
        self.urls = url_manager.UrlManager() #url管理器
        self.downloader = html_downloader.HtmlDownloader() #下载器 
        self.parser = html_parser.HtmlParser() #解析器
        self.outputer = html_outputer.HtmlOutputer() #输出器
        
    def craw(self,rootUrl):    #爬取函数
        count = 1
        self.urls.addNewUrl(rootUrl) #添加链接
        while self.urls.hasNewUrl(): #存在未爬链接（即新链接）
            try:
                newUrl = self.urls.getNewUrl() #取一个新链接
                print('craw %d : %s' % (count,newUrl))
                htmlCont = self.downloader.download(newUrl) #下载网页内容
                nextUrl,listUrls = self.parser.parse(newUrl,htmlCont) #解析网页内容，获取新链接数组和所需爬取信息
                #取详情页链接
                for  detailUrl in listUrls:
                    detailCont = self.downloader.download(detailUrl) #下载网页内容
                    detailData = self.parser.parseDetail(detailUrl,detailCont)
                    self.outputer.collectData(detailData) #保存所需爬取信息
                      
                self.urls.addNewUrl(nextUrl) #保存新链接（待爬取链接）
              
                
                if count == 100: 
                    break
                count = count + 1
            except Exception as e:
                print('craw failed：'+str(e))
        
        self.outputer.insert_to_mysql() #输出到html
                


if __name__=="__main__":
    rootUrl = "http://www.xcl555.com/ribenAV/"
    obj_spider = SpideMain()
    obj_spider.craw(rootUrl)