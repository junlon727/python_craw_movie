'''
Created on 2018年2月26日

@author: Administrator
'''
from bs4 import BeautifulSoup
import urllib




class HtmlParser(object):
    #p_node = soup.find('p',class_="title")
    #print(p_node.name,p_node.get_text())
    def getNextUrl(self,pageUrl,soup):
        link = soup.find("div",class_="pagenav").find('a',text="下一页")
        url = link['href']
        full_url = urllib.parse.urljoin(pageUrl,url)
        return full_url
        
        
    def getListUrls(self,pageUrl,soup):
        urls = set()
        links = soup.find("div",class_="mbox").find_all("h4",class_="rtl")
        for link in links:
            url = link.find('a')['href']
            full_url = urllib.parse.urljoin(pageUrl,url)  #拼成完整url
            urls.add(full_url)
        return urls
     
    def getDetailData(self,pageUrl,soup):
        data = {}
        title = soup.find("div",class_="list").find('h1').find('a').get_text() #标题
        data['title'] = title
        
        cover = soup.find("div",class_="list").find('img')['src']  #封面
        data['cover'] = cover
        
        decpts = soup.find_all("div",class_="pbox")
        for dept in decpts:
            if dept.find('p') is not None:
                data['decpt'] = dept.find('p').get_text() #描述
                break
        purl = soup.find("div",class_="pbox").find('a')['href'] #播放地址
        playurl = urllib.parse.urljoin(pageUrl,purl)
        data['playurl'] = playurl
        
        stills = soup.find("div",class_="list").find('img',class_="vodimg_b")['src'] #剧照
        data['stills'] = stills
        
        return data   

    def parse(self,pageUrl,htmlCont):
        if pageUrl is None or htmlCont is None:
            return
        soup = BeautifulSoup(htmlCont,'html.parser',from_encoding='utf8')
        #BeautifulSoup是Python的一个库，最主要的功能就是从网页爬取我们需要的数据。
        newUrl = self.getNextUrl(pageUrl,soup)
        listUrls = self.getListUrls(pageUrl,soup) 
        return newUrl,listUrls

    def parseDetail(self,pageUrl,cont):
        if pageUrl is None or cont is None:
            return
        soup = BeautifulSoup(cont,'html.parser',from_encoding='utf8')
        detailData = self.getDetailData(pageUrl,soup)
        return detailData
