'''
Created on 2018年2月26日

@author: Administrator
'''
import urllib

from pip._vendor.requests.api import request

class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return
        try:
            response = urllib.request.urlopen(url,timeout=10)
            if response.getcode() != 200: #200:success
                return None
            return response.read()
        except Exception as e:
            print('An error occurred while downloading: '+str(e))

