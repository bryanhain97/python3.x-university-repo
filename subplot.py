# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:36:12 2021

@author: seher
"""



import matplotlib.pyplot as plt



def createsubplot(x,y,startprozent,endprozent):

       startprozent=float
       endprozent=float
       z=len(x)
       
       
       plt.plot(x,y,label="Graph",)
       plt.xlabel=("x in π")
       plt.ylabel=("y")
       plt.xlim((z*startprozent)/100, (z*endprozent)/100)

       plt.title=("Plot")
       plt.legend()
       plt.savefig("plot.pdf", format="pdf")
       plt.show()


def create_subplot(x, y, startprozent, endprozent):
       # startprozent, endprozent sind Floats und x,y sind Listen
       # 1. Anzahl der Elemente von X und Y bestimmen; vorausgesetzt: len(x) == len(y)
       länge = len(x)
       länge_prozent = länge / 100                             #länge von x,y = 500; 1% == 5 elemente

       # 2. X,Y - Werte sind skaliert, aber Bereich muss noch ausgeschnitten werden
       # Da Liste[2.3] nicht möglich => runden

       # annahme: übergebenes X hat 120 elemente:
       anfang = round(startprozent, 0) * länge_prozent         # startprozent = 23.5% ==> 23 * 5 elemente 
       ende = round(ende, 0) * länge_prozent                   # endprozent = 84.6% ==> 85 * 5 elemente 
       plt.pyplot(x[anfang:ende], y[anfang:ende])
       plt.xlabel("x-Achse, skaliert")
       plt.ylabel("y-Achse, skaliert")
       plt.title("Graph")
       plt.legend()
       plt.savefig("plot.pdf", format="pdf")
       plt.show()