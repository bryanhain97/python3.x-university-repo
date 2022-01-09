import csv
from subplot import create_subplot
import matplotlib as plt


x=[]
y=[]


while True:
    dateiname = input("CSV-Datei einlesen: ")
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            zeilen = csv.reader(datei, delimiter=";")
            for zeile in zeilen:
                x.append(float(zeile[0]))
                y.append(float(zeile[1]))
        break
    except FileNotFoundError:
        print("Datei wurde nicht gefunden, bitte erneut eingeben.")
# DATEI.CSV EINLESEN




while True:
    try:
        skalierung = float(input("Skalierungsfaktor eingeben: "))
        break
    except ValueError:
        print("Skalierungsfaktor muss vom Typ Float sein!")
# SKALIERUNGSFAKTOR EINLESEN



y_scaled = []
for wert in y:
    y_scaled.append(wert * skalierung)
print(y_scaled)
# SKALIERUNG DER Y LISTE




while True:
    try:
        startProzent = float(input("Bitte Startprozent eingeben: "))
        if(startProzent >= 0 and startProzent <=100):
            break
        else:
            print("Startprozent sollte innerhalb (0-100) liegen!")
    except ValueError:
        print("Startprozent muss vom Typ Float sein!")
# STARTPROZENT ABFRAGEN




while True:
    try:
        endProzent = float(input("Bitte Endprozent eingeben: "))
        if(endProzent >= startProzent and endProzent > 0 and endProzent <= 100):
            break
        print("Endprozent muss größer als Startprozent sein und innerhalb (0-100) sein!")
    except ValueError:
        print("Endprozent muss vom Typ Float sein!")
# ENDPROZENT ABFRAGEN
        

create_subplot(x,y_scaled,startProzent,endProzent)