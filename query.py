# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:20:34 2019

@author: icecream boi
"""

import pandas as pd 
import random 
from datetime import datetime
	
df = pd.read_csv('songs.csv', sep=';')
  
df.columns = ['author', 'date', 'lyrics','user', 'title', 'num_views']

import ast

df.lyrics = df.lyrics.apply(ast.literal_eval)

  
def selection(df):
    
    return df

def pick_lyric(df):
    index_value = random.randrange(len(df))
    selected_row = df.loc[index_value, :] 
    selected_row['lyrics'] = random.choice(selected_row['lyrics'])

    return dict(selected_row)
#df = selection(df)
    
values = pick_lyric(df)

author = values['author']
title = values['title']
lyrics = values['lyrics']

from PIL import Image, ImageDraw, ImageFont

img = Image.open('bcg.png')
canvas = ImageDraw.Draw(img)
font = ImageFont.truetype('Avojaloin.ttf', size=55)
text_width, text_height = canvas.textsize(lyrics, font=font)

if text_width <= 900 and text_height <= 1200:
    
    astr = lyrics
    para = astr.split('\n')
    MAX_W, MAX_H = 1080, 1350
    im = img = Image.open('bcg.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Avojaloin.ttf', size=55)
    
    current_h = (MAX_H - text_height-100)/2
    pad =  15
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w ) / 2, current_h), line, font=font, fill=(0,0,0,0))
        current_h += h + pad
    
    lfname = 'logo.png'
    limage = Image.open(lfname)
    
    box = (int(MAX_W / 2)-50, int(current_h+50))
    im.paste(limage, box)

    
    im.save('test.png')
    
else:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    len_of_lyrics = len(str(values['lyrics']))
    value = dt_string + ' ' + 'len_of_lyrics: ' + str(len_of_lyrics)# + song
    with open("log.txt", "a") as text_file:
        text_file.write(value)
        text_file.write('\n')
        













