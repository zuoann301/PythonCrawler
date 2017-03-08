# -*- coding:utf-8 -*-
import urllib
import re
import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError

import xlrd
import xlwt
import datetime
from bs4 import BeautifulSoup

from pandas import DataFrame, Series
from multiprocessing.dummy import Pool as ThreadPool
import pandas as pd

import time
from time import ctime,sleep
from threading import Timer
import sys,traceback
import random

#err_urls=[]

def GetHtmlCode(url):
    #print(urllib.parse.urlparse(url).query)
    #params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    #print('正在解析第{0}页...'.format(params.get('PageID', [''])[0]))
    #'http://www.nongnet.com/listqiye.aspx?PageID=2'
    #ip_arr=["110.72.25.86:8123","171.38.202.200:8123","219.152.117.107:8888","182.88.253.185:8123","182.90.119.142:80","124.66.51.33:8090","110.73.6.95:8123"]
    #random.shuffle(ip_arr)
    #random_ip=ip_arr[0]
    #print("*******************"+random_ip+"***********************")
    #proxy_support = urllib.request.ProxyHandler({'HTTP': random_ip})
    #opener = urllib.request.build_opener(proxy_support)
    #urllib.request.install_opener(opener)
    page_data=urllib.request.urlopen(url).read()#.decode("UTF-8")
    #print(page_data)
    #req = urllib.request.Request(url, headers = {
    #'Connection': 'Keep-Alive',
    #'Accept': 'text/html',
    #'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    #})
    
        
    
    return page_data

####################################################
def GetItemList(url,page):
    #LISTA=[]
    url1=urllib.parse.unquote(url) #/xinxi/270474.aspx
    #xinxi_id=url1.replace("http://www.nongnet.com","").replace("/xinxi/","").replace(".aspx","")
    #link_url=url1.replace("http://www.nongnet.com","")
    
    html_code=GetHtmlCode(url)
    if(html_code==""):
        LISTA.append([page,""])
    else:
        soup = BeautifulSoup(html_code,'html.parser')

        #page_title=soup.title.get_text();
        #page_keywords=soup.head.find_all(attrs={'name':'keywords'})[0].get("content")
        #page_description=soup.head.find_all(attrs={'name':'description'})[0].get("content")
        #print("title:"+page_title)
        #print("keywords:"+page_keywords)
        #print("description:"+page_description)

        
        
        
        #table = soup.findAll(name="tr", attrs={"class":re.compile(r"tr(\s\w+)?")});
        #div_title = soup.findAll(name="div", attrs={"class":"xinxisx"});
        item_list = soup.findAll(name="div", attrs={"class":"cn_box2"});
        #page_sort=soup.findAll(name="div", attrs={"class":"Title_list"});

        #print(page_sort[0].get_text())
        
        for item in item_list:
            #img=item.find('img').get('src')
            link=item.find('a').get('href')
            #print(img)
            #print("http://www.meijutt.com"+link)
            content_url="http://www.meijutt.com"+link
            LISTA.append([page,content_url])
        
        #div_content=soup.findAll(name="font", attrs={"color":"999999"})
        #a_content=soup.findAll(name="a", attrs={"class":"f12dh"})
        #f12dh
        #print(div_content[0].get_text())
        #if(div_content!='' and a_content!=''):
        #    font_text=div_content[0].get_text()
        #    arr=font_text.split('     ')
        #    
        #    ctime=arr[0].replace("时间","").replace("：","").strip()
        #    hits=arr[1].replace("浏览人数","").replace("：","").strip()
        #    sort=a_content[1].get_text().strip().replace(" ","")
        #   print(ctime)
        #    print(hits)
        #    print(sort)
        #else:
        #    LISTA=[xinxi_id,link_url,"","",""]
    
        
    #return LISTA
###########################################   
def savelog(txt):
    f=open("log.txt","a")
    f.write("------------------"+str(datetime.datetime.now())+"------------------------\r\n")
    f.write(txt)
    f.write("\r\n")
    f.close()
###########################################
def soundStart(s):
    soundFile = 'chord.wav'
    soundFile2 = 'Ring10.wav'
    if sys.platform[:5] == 'linux':
        import os
        os.popen2('aplay -q' + soundFile)
    else:
        import winsound
        if(s=="1"):
            winsound.PlaySound(soundFile, winsound.SND_FILENAME)
        else:
            winsound.PlaySound(soundFile2, winsound.SND_FILENAME)
###########################################
LISTA=[]

if __name__=='__main__':
    starttime = datetime.datetime.now()
    #LISTA=[]

    

    PageStartIndex = input('请输入起始页码')
    PageEndIndex = input('请输入结束页码')
    int_PageStartIndex=int(PageStartIndex)
    int_PageEndIndex=int(PageEndIndex)+1
    
    #data = xlrd.open_workbook('test.xls')
    #table = data.sheets()[0]
    #nrows = table.nrows
    #ncols = table.ncols
    #colnames =  table.row_values(0)

    #print('总行数：'+str(nrows))
    #print('总列数：'+str(ncols))
    #print('表头：'+colnames[0]+' '+colnames[1])

    arr_url=[]
    for i in range(int_PageStartIndex,int_PageEndIndex):
        print(i);
        if(i==1):
           arr_url.append("http://www.meijutt.com/file/list6.html")
        else:
            arr_url.append("http://www.meijutt.com/file/list6_"+str(i)+".html")

    print("总页数：")
    print(len(arr_url))
    

    

    FileName="data.csv"
    temp_index=1
    try:
        for url in arr_url:
            #row = table.row_values(rownum)
            #key=row[1].replace(" ","")
            #if row:
            #url='http://www.meijutt.com/file/list2_'+str(rownum)+'.html'
            #print("----------------------"+str(rownum)+"--------------------")
            print("路径："+url+"")
            temp_data=GetItemList(url,temp_index)
                 #print(temp_data)
                 #temp_index=rownum
            #LISTA.append(temp_data)
            time.sleep(3)
            temp_index=temp_index+1
    except Exception as err:
        print("----------------error start-----------------")
        #print(len(LISTA))
        FileName="time_"+PageStartIndex+"-"+str(temp_index)+".csv"
        pdaa = pd.DataFrame(LISTA)
        #pdaa.columns = ["page","url"]
        pdaa.to_csv(FileName)
        print(err)
        print("----------------error end-----------------")
         
    print(len(LISTA))
    pdaa = pd.DataFrame(LISTA)
    pdaa.columns = ["page","url"]
    pdaa.to_csv(FileName)
    
    endtime = datetime.datetime.now()

    #print(err_urls)
    soundStart("2")
    print("执行时间："+str((endtime - starttime).seconds))


    
