# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:33:56 2021

@author: seher
"""
import csv
import subplot
import matplotlib as plt



x=[]
y=[]


while True :
    dateiname=input("CSV Dateiname: ")
    
    try:
        with open(dateiname,"r",encoding="utf-8") as datei:
            reader=csv.reader(datei,delimiter=";")
            for row in reader:
                x.append(float(row[0]))
                y.append(float(row[1])) 
           
        break
    except FileNotFoundError:
        print("Datei wurde nicht gefunden. Bitte erneut einen Dateinamen eingeben.")

       
while True :
    skalierung=(input("Skalierungsfaktor: "))
    
    try:
        float(skalierung)
        break
    except ValueError:
        print("Der Skalierungsfaktor muss vom Typ Float sein.")

while True:
    startprozent=(input("Start Prozent: "))

    
    try:
         float(startprozent)
         if 0 <= float(startprozent) <=100:
             break
         else:
             print("Es werden Floats zwischen 0-100 erwartet.")
             

    except ValueError:
        print("Es werden Floats als Eingabe erwartet.")


            
    
while True:
    endprozent=(input("End Prozent: "))

    
    try:
         float(endprozent)
         if 0 <= float(endprozent) <=100:
             break
         else:
           print("Es werden Floats zwischen 0-100 erwartet.")
     
    except ValueError:
        print("Es werden Floats als Eingabe erwartet.")


for wert in x:
    wert = wert * skalierung
for wert in y:
    wert = wert * skalierung
# MODIFY all array
subplot.createsubplot(x,y,startprozent,endprozent)