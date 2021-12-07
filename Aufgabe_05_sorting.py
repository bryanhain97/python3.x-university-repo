# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:59:59 2021

@author: seher
"""

mix=[51, 0, "Q", "LISTE", 4.3, {"null" : 0, "eins" : 1, "zwei" : 2}, -1, "Tupel", 1, "False", 3 > 5, "hell", 666, "dictionaries", True, 42.42]

ints=[]
strings=[]
doubles=[]
dicts=[]
summe=0

for val in (mix) :
   
    if type(val)==int:
      ints.append(val)
      summe+=val
    elif type(val)==str:
      strings.append(val)
    elif type(val)==float:
      doubles.append(val) 
      summe+=val
    elif type(val)==dict:
      dicts.append(val)
    else:
      break


# Ausgaben der Listen 
print("Sortierte Listen: ")
print(ints)
print(doubles)
print(strings)
print(dicts)

# Ausgabe der Summe von allen eingelesenen Zahlen
print(summe)

 

        
        
        
