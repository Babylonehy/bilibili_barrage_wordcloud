#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:44:13 2017

@author: lixiang

'''
background_color='#F0F8FF',      # 参数为设置背景颜色,默认颜色则为黑色
font_path="HYQiHei-80S.otf", # 使用指定字体可以显示中文，或者修改wordcloud.py文件字体设置并且放入相应字体文件
max_words=1000,  # 词云显示的最大词数
font_step=10,    # 步调太大，显示的词语就少了
mask=color_mask,  #设置背景图片
random_state= 15, # 设置有多少种随机生成状态，即有多少种配色方案
min_font_size=15,  #字体最小值
max_font_size=232, #字体最大值
'''
"""
import jieba,jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import os

import numpy as np
from PIL import Image

def word_cloud(dirtxt,encoding='utf-8',mask_switch='on',mask_name='',name='',fontpath='',save_path='',colorset='on'):
    with open(dirtxt,'r',encoding=encoding) as f:
        text = f.read()
        f.close()
    cut_text = " ".join(jieba.cut(text))  #使用空格连接 进行中文分词
    if (mask_switch=='on'):
        color_mask = np.array(Image.open(os.path.join(dirtxt,mask_name)))   # 设置图片
        cloud = WordCloud( background_color='white',font_path=fontpath,mask=color_mask,random_state= 500)
        cloud.generate(cut_text)  #对分词后的文本生成词云
        if (colorset=='on'): 
            image_colors = ImageColorGenerator(color_mask)  # 从背景图片生成颜色值
            plt.show(cloud.recolor(color_func=image_colors))  # 绘制时用背景图片做为颜色的图片
    else:
        cloud = WordCloud( background_color='white',font_path=fontpath,random_state= 500)
        cloud.generate(cut_text)  #对分词后的文本生成词云
              
    
    plt.imshow(cloud)            # 以图片的形式显示词云
    plt.axis('off')                     # 关闭坐标轴
    plt.show()                          # 展示图片   
    cloud.to_file(os.path.join(save_path, name+'词云.png'))  # 图片大小将会按照 mask 保存

'''
word_cloud(fontpath='/Users/lixiang/Desktop/Github/douyudanmu/HYQiHei-80S.otf',
           dirtxt='/Users/lixiang/Desktop/Github/douyudanmu/弹幕/687423danmu.txt',
           save_path='/Users/lixiang/Desktop/Github/douyudanmu/',
           mask_switch='on',
           mask_name='/Users/lixiang/Desktop/Github/douyudanmu/overwatch.png',
           encoding='gbk',
           colorset='off'
           )
'''