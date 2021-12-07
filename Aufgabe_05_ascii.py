# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:13:54 2021

@author: seher
"""


height=int(input("Bitte Höhe eingeben: "))
width=int(input("Bitte Breite eingeben: "))

height2=height+2
width2=width+2


for j in range(height2):
    for l in range(width2):
        if j==0 or j==height2-1 or l==0 or l==width2-1:
              print("C",end=" ")
        else:
             print("A", end=" ")
    print()