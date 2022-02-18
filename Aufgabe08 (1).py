# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:41:43 2022

@author: seher
"""
import math

class Point:
    counter=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        type(self).counter += 1
        
        
    def __del__(self):
        type(self).counter -= 1
        
    def move(self,dx,dy):
        self.x = dx + self.x
        self.y = dy + self.y
        
    def coincide(self, point2):                      
        if  self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False
        
    def print(self):
        print(f"Punkt bei ({self.x},{self.y})")
            
            
class Circle(Point):
    def __init__(self,x,y,radius):
        self.radius = radius
        super().__init__(x,y)
        

    
    def coincide(self, point2):
        self.dist_circlecenter_point2 = math.sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2)
        if self.dist_circlecenter_point2 <= self.radius:
            return True
        else:
            return False           
            
    def print(self):
        print(f"Kreismitte bei: ({self.x},{self.y})\n Radius:{self.radius} ")
           
class LineSeg:
    
    def __init__(self,start,end):
        self.p1 = start
        self.p2 = end
    

    def p_on_line(self,point3):
        self.dist_start_end = math.sqrt((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)
        self.dist_start_point3 = math.sqrt((self.p1.x - point3.x)**2 + (self.p1.y - point3.y)**2)
        self.dist_end_point3 = math.sqrt((self.p2.x - point3.x)**2 + (self.p2.y - point3.y)**2)
        if self.dist_start_end == self.dist_start_point3 + self.dist_end_point3:
            return True
        else:
            return False
        
    def print(self):
        print(f"Anfangspunkt bei: ({self.p1.x},{self.p1.y}) \n Endpunkt bei: ({self.p2.x},{self.p2.y}) ")
        
            
            