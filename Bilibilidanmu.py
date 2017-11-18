#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:56:14 2017

@author: lixiang
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from word_cloud import word_cloud

def gettitle(av=0):
      header={
              'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'        
        } 
      url='https://www.bilibili.com/video/av'+str(av)
      data = requests.get(url, headers=header) 
      soup = BeautifulSoup(data.text, 'lxml')  
      title=soup.find('h1').get('title')
      #print(title)
      return title
def get_cid(av=0):
    url='https://api.bilibili.com/x/player/pagelist?aid='+str(av)+'&jsonp=jsonp'
    header={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'        
        } 
    r = requests.get(url, headers=header)
    html=r.content.decode('utf-8')
    avinfo=json.loads(html)
    cid=avinfo['data'][0]['cid']
    return cid
    #print(str(cid))

def download_danmu(av=0,cid=0):
    d = os.path.dirname(__file__)
    output = open(d+'/弹幕/'+str(gettitle(av))+'.txt', 'w')
    url='https://comment.bilibili.com/'+str(cid)+'.xml'
    header={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'        
        } 
    data = requests.get(url, headers=header) 
    soup = BeautifulSoup(data.text, 'lxml')  
    danmu=soup.find_all('d')
    count=0
    for each in danmu:
        output.write(each.get_text()+'\n')
        count=count+1
        #print(each.get_text())
    print('-----'+str(gettitle(av))+'-----['+str(count)+']弹幕加载完毕!')


av=16368916
if __name__ == '__main__':
    av = input('请输入av号:')
    download_danmu(av,get_cid(av))
    d = os.path.dirname(__file__)
    word_cloud(fontpath='HYQiHei-80S.otf',
               dirtxt=d+'/弹幕/'+str(gettitle(av))+'.txt',
               save_path=d+'/弹幕词云/',
               mask_switch='off',
               mask_name='/Users/lixiang/Desktop/images.png',
               name=gettitle(av),
               encoding='utf-8',
               colorset='on'
               )
    
    
    