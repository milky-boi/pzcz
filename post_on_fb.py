# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 02:05:29 2019

@author: icecream boi
"""
"""
import facebook

page_access_token = "EAAiWqlM1abABAB7FqQSqkwSZAKHMUC4lQ4mzLLHd5lhwoCgK3klIuw0MnaEaOhtSokRx9U9a7lMrELLCGwmvmgFMFgzdrx6QBQwfSEEseR6GZBvk3OpCC2Sx5iC1R22R1coriwdzjUEcJKYZCGWabmg6xSVyZB20ZATjrZAswwUnY8ty7f5PsZCb4iaEwJZB4oZCFqmmEl18fegeHG0ScYrGi"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "317007308335028"
photo = open("test.png", "rb")
graph.put_object("me",
                 "photos",
                 message="You can put a caption here",
                 source=photo.read())
photo.close()
"""
from poster.encode import *
from poster.streaminghttp import register_openers



