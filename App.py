#!/usr/bin/env python
# -*- coding: utf-8 -*-

###python 2.7.11
##安装两个组件
##pip install bs4
##pip install Requests


import datetime
import threading
from threading import Timer
import requests
import json
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout,ConnectionError,RequestException

##获取网页抽取位置
def get_html(url):
    try:
        response = requests.get(url)
        content=response.content.decode("gb2312","ignore")
        soup=BeautifulSoup(content,'html.parser')
        htmlcontent= soup.find(id='zhishu').find("ul",attrs={"class":"zhishu_ul"})
    except ReadTimeout:
        print("timeout")
    except ConnectionError:
        print("connection Error")
    except RequestException:
        print("error")
    return htmlcontent

##转换定义格式化数据（可以多种数据源）
def parse_html(content):
    result="";
    list = content.find_all("div")
    for m in list:
        result+=m.p.text.encode('utf-8')+":"+m.h5.text.encode('utf-8')+"\n"
    return result

##写入文件
def write_to_file(content):
    with open("result.txt",'w') as f:
        f.write(content)

##入口函数
def main():
    url="http://www.zhue.com.cn/"
    content= get_html(url)
    result=parse_html(content)
    write_to_file(result)
    print "task is done"
    print datetime.datetime.now();

if __name__=="__main__":
    main()