# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 02:38:08 2019

@author: icecream boi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:47:13 2019

@author: icecream boi
"""
import os
import pandas as pd 

all_articles = os.listdir(r'C:\Users\icecream boi\Desktop\pycy\r1')

#all_articles = all_articles[:100]
#all_articles = os.listdir(r'C:\Users\icecream boi\Desktop\article_tags\articles')

df = pd.DataFrame(columns = ['author', 'title', 'num_views',
                             'lyrics', 'user', 'date']) 
all_dicts = []
fail = []
for entry in all_articles:
    file = open(str('r1/' + entry))
    try:
        
        file = eval(file.read())
        if len(file) == 6:
            all_dicts.append(file)
    
    except SyntaxError:
        fail.append(file)
        print(len(fail))    
    
    
df = pd.DataFrame(all_dicts)
   
df.to_csv('songs.csv', sep=';', encoding='utf-8', index=False)
            