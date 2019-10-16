# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:48:56 2019

@author: icecream boi
"""


from PIL import Image, ImageDraw, ImageFont
import os 

image_width = 350
image_height = 70

img = Image.new('RGB', (image_width, image_height), color=(51, 144, 255))

# create the canvas
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('Lato-Bold.ttf', size=24)

text_width, text_height = canvas.textsize('Hello World', font=font)

print(f"Text width: {text_width}")
print(f"Text height: {text_height}")


x_pos = int((image_width - text_width) / 2)
y_pos = int((image_height - text_height) / 2)

print(f"X: {x_pos}")
print(f"Y: {y_pos}")


canvas.text((x_pos, y_pos), "Hello World", font=font, fill='#FFFFFF')

img.save('pil_text.png')

