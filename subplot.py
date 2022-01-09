# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:36:12 2021

@author: seher
"""


import matplotlib as plt
import math

def create_subplot(x,y,start,end):
    
    #Ausschnitt start-end berechnen
    len_xy_percent = math.floor(len(x)/100)
    start = math.floor(start)*round(len_xy_percent,0)
    end = math.ceil(end)*round(len_xy_percent,0)
    plot_x = x[start:end]
    plot_y = y[start:end]
    print(plot_x, plot_y) # gibt  X-bereich und zugehörigen Y-Werte aus, len(x) == len(y)
    
    # Graph bauen aus plot_x und plot_y
    # Achsenbeschriftung mit plot_x, plot_y