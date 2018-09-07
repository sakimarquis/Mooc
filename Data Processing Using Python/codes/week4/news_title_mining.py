# -*- coding: utf-8 -*-
"""
Basic idea of the program:
     1. Grab a few webpages from sina and extract the news subjects
     2. Segment words using Python the package jieba
         2.1 Filter out the stop words
         2.2 Only keep nouns
     3. Load all the words(with some appearing multiple times) into the package wordcloud
     4. That's it!

@author: Dazhuang
	 
"""

import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import re
import requests
from scipy.misc import imread
import time
from wordcloud import WordCloud

def fetch_sina_news():
    PATTERN = re.compile('.shtml" target="_blank">(.*?)</a><span>(.*)</span></li>')
    BASE_URL = "http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_"
    MAX_PAGE_NUM = 2

    with open('subjects.txt','w',encoding='utf-8') as f:
        for i in range(1, MAX_PAGE_NUM):
            print('Downloading page #{}'.format(i))
            r = requests.get(BASE_URL + str(i)+'.shtml')
            r.encoding='gb2312'
            data = r.text
            p = re.findall(PATTERN, data)
            for s in p:
                f.write(s[0])
            time.sleep(5)
    
def extract_words():
    with open('subjects.txt','r',encoding='utf-8') as f:
        news_subjects = f.readlines()
    
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    
    newslist = []
    
    for subject in news_subjects:
        if subject.isspace():
            continue
        
        # segment words line by line
        word_list = pseg.cut(subject)     
        for word, flag in word_list:
            if not word in stop_words and flag == 'n':
                newslist.append(word)
    
    d = path.dirname(__file__)
    mask_image = imread(path.join(d, "mickey.png"))

    content = ' '.join(newslist)
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", mask=mask_image, max_words=40).generate(content)
    
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
    
if __name__ == "__main__":
    fetch_sina_news()
    extract_words()
