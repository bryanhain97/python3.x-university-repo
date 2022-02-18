# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:20:32 2022

@author: seher
"""
import matplotlib.pyplot as plt
import csv

x=[]
y=[]


with open("Raw_Data.csv","r", encoding="utf-8") as datei:
            zeilen = csv.reader(datei, delimiter=";")
            i = 0
            for zeile in zeilen:
                if i == 0:
                    i += 1
                    continue
                
                x.append(float(zeile[0]))
                y.append(float(zeile[1]))
                i += 1
                
x_scaled = []
for wert in x:
       x_scaled.append(wert /60)
       




plt.plot(x_scaled, y,label="Graph") 
             
plt.xlabel("t in min")  
plt.ylabel("Sensorwert") 

    #Titel 
plt.title("Aufzeichnung der Helligkeit vom 25.01.22 von 16:35-17:08")

    #Vertikale Linien für Ereignisse setzen
plt.axvline(x=4,color="red",linestyle="-.",label="Sonnenuntergang 16:39h")
#plt.axvline(x=4,color="red",linestyle="-.-",label="Sonnenuntergang 16:39h")
plt.legend()    
    #speichern und plotten
plt.savefig("plot.pdf", format="pdf")
plt.show()
