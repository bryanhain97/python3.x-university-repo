# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:41:43 2022

@author: seher
"""
import math

class point:
    counter=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        type(self).counter += 1
        
        
    def __del__(self):
        type(self).counter -= 1
        
    def move(self,dx,dy):
        self.x=dx+self.x
        self.y=dy+self.y
        
    def coincide(self, point2):                        
        if  self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False
        
    def print(self):
        print(f"Dies ist eine Instanz der Klasse {type(self)} mit x = {self.x} und y = {self.y}")
            
            
class cirle(point):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return math.pi*(self.radius**2)   
         
    def coincide(self, point2):
        if (point2.x <= self.x + self.radius and point2.y <= self.y + radius):
            return True
        else:
            return False           
            
    def print(self):
        print(f"Kreismitte bei: ({0},{1}) \n Radius:{3} ")
           
class lineSeg:
    
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    
    def length(self):
        return math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
    
   
    def p_on_line(self,a,b):
        if (a,b) in self.line:
            return True
        else:
            return False
        
    def print(self):
        print(f"Anfangspunkt bei: ({self.x1},{self.y1}) \n Endpunkt bei: ({self.x2},{self.y2}) ")
        
            
            