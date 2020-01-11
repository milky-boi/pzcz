# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:20:34 2019

@author: icecream boi
"""

import pandas as pd 
import random 
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import ast
from facepy import GraphAPI

def pick_lyric(df):
    index_value = random.randrange(len(df))
    selected_row = df.loc[index_value, :] 
    selected_row['lyrics'] = random.choice(selected_row['lyrics'])

    return dict(selected_row)

def create_image(values, number):
    author = values['author']
    title = values['title']
    lyrics = values['lyrics']
    
    img = Image.open('bcg.png')
    canvas = ImageDraw.Draw(img)
    font = ImageFont.truetype('Raleway-Bold.ttf', size=55)
    text_width, text_height = canvas.textsize(lyrics, font=font)
    
    if text_width <= 900 and text_height <= 800:
        if len(lyrics) > 10:
            astr = lyrics
            para = astr.split('\n')
            MAX_W, MAX_H = 1080, 1350
            im = img = Image.open('bcg.png')
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('Raleway-Bold.ttf', size=55)
            
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
        
            image_name = 'output/' + author + ' - ' + title + '.png'
            im.save(image_name)
            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            len_of_lyrics = len(str(values['lyrics']))
            value = dt_string + ';' + 'True;' + 'len: ' + str(len_of_lyrics) + ';' + author + ';' + title + ';' + str(lyrics.split('\n'))
            with open("log.csv", "a") as text_file:
                text_file.write(value)
                text_file.write('\n')
                
        else:
            now = datetime.now()
            astr = lyrics
            para = astr.split('\n')
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            len_of_lyrics = len(str(values['lyrics']))
            value = dt_string + ';' + 'False;' + 'len: ' + str(len_of_lyrics) + ';' + author + ';' + title + ';' + str(lyrics.split('\n'))
            with open("log.csv", "a") as text_file:
                text_file.write(value)
                text_file.write('\n')
                              
    else:
        now = datetime.now()
        astr = lyrics
        para = astr.split('\n')
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        len_of_lyrics = len(str(values['lyrics']))
        value = dt_string + ';' + 'False;' + 'len: ' + str(len_of_lyrics) + ';' + author + ';' + title + ';' + str(lyrics.split('\n'))
        with open("log.csv", "a") as text_file:
            text_file.write(value)
            text_file.write('\n')
 


def post_on_facebook(image):
    print ('Trying Facebook page...')
    my_token = 'EAAj9utB7DlUBAFz01dd4N3pXVzszNtYHF7GE8eVNZC3c8WTjB4JZCC8xFkYP0VUGI85nkjogvg1Q2UuObw68v6TLU0mvNn7nsUwYVXefZCABvWmLdSwp7hCY17rhaLZArcQUyQsxl9jj9oyeOii0BSqZByOrrPZCjnSviY2FTwRxO3OLYRW0TO'
    graph = GraphAPI(my_token) 
    # Get my latest posts
    #my_posts = graph.get("me/posts")    
     #Post a photo of a parrot
    graph.post(path = "100375534755582/photos",source = image)#open("picture.png", "rb"))    
    print ('Done.')

def main():       
    df = pd.read_csv('songs.csv', sep=';')
      
    df.columns = ['author', 'date', 'lyrics','user', 'title', 'num_views']
    
    df.lyrics = df.lyrics.apply(ast.literal_eval)
    
    for i in range(100):
        values = pick_lyric(df)      
        image = create_image(values, i)
        #post_on_facebook(image)
        
if __name__ == '__main__':
    main()











