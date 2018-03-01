'''
Created on 2018年2月26日

@author: Administrator
'''
import pymysql
import json
from test.test_audioop import datas
from idlelib.iomenu import encoding


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collectData(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def insert_to_mysql(self):
        conn = pymysql.Connect(
                       host = 'localhost', #本地mysql地址
                       port = 3306,  #端口
                       user = 'root',   #用户名
                       passwd = 'root', #密码
                       db = 'python',   #数据库
                       charset = 'utf8' #字符
                       )
        cursor = conn.cursor()   #获取游标对象
    
        try:

            with open("data.json", 'w',encoding='utf8') as fw:
                msg = [json.dumps(d,ensure_ascii=False)  for d in self.datas]
                fw.write("\n".join(msg))
            """
            cursor.execute("delete from movie")
            for data in self.datas:
                #print(data['title'],data['cover'],data['decpt'],data['playurl'],data['stills'])
                sql = "insert into movie values(null,%s,%s,%s,%s,%s)"  % (repr(data['title']),repr(data['cover']),repr(data['decpt']),repr(data['playurl']),repr(data['stills']))
                cursor.execute(sql)
                conn.commit()    """
        except Exception as e:
            print("An error occurred while inserting："+str(e))
            #conn.rollback()
        finally:
            cursor.close()
            conn.close()

