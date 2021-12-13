# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:40:23 2021

@author: seher
"""



def benotung(notenschluessel,punkte):
    if notenschluessel== 1 :
        if punkte <50:
         note= 5.0
        elif punkte <=53:
         note= 4.0
        elif punkte <=57:
         note= 3.7
        elif punkte <=61:
         note= 3.3
        elif punkte <=65:
         note= 3.0
        elif punkte <=69:
         note= 2.7
        elif punkte <=73:
         note= 2.3
        elif punkte <=77:
         note= 2.0
        elif punkte <=81:
         note= 1.7
        elif punkte <=85:
         note= 1.3
        else:
         note= 1.0
         
    elif notenschluessel== 2 :
       if punkte<50:
        note= 5.0
       elif punkte <=54:
        note= 4.0
       elif punkte <=98:
        note= 3.7
       elif punkte <=64:
        note= 3.3
       elif punkte <=69:
        note= 3.0
       elif punkte <=74:
        note= 2.7
       elif punkte <=79:
        note= 2.3
       elif punkte <=84:
        note= 2.0
       elif punkte <=89:
        note= 1.7
       elif punkte <=94:
        note= 1.3
       else:
        note= 1.0
        
    elif notenschluessel== 3 :
      if punkte <40:
        note= 5.0
      elif punkte <=44:
        note= 4.0
      elif punkte <=49:
        note= 3.7
      elif punkte <=54:
        note= 3.3
      elif punkte <=59:
        note= 3.0
      elif punkte <=64:
        note= 2.7
      elif punkte <=69:
        note= 2.3
      elif punkte <=74:
        note= 2.0
      elif punkte <=79:
        note= 1.7
      elif punkte <=84:
        note= 1.3
      else:
        note= 1.0
        
    bestanden = note <= 4.0

        
    return note,bestanden



student_i_matrikelnummer=[]
student_i_punkte=[]

notenschluessel=int(input("Notenschlüssel: "))
if notenschluessel== 1 or 2 or 3:
    while True:
        matrikelnummer=int(input("Matrikelnummer: "))
        punkte=float(input("Punkte: "))
        student_i_matrikelnummer.append(matrikelnummer)
        student_i_punkte.append(punkte)
    
      
        weitere_eingabe=input("Weitere Eingabe: ")
        if weitere_eingabe !=  "ja" :
            break

    print("Matrikelnummer\tPunkte\tNote\tBestanden")    
    for i,matrikelnummer in enumerate(student_i_matrikelnummer):
          student_i_punkte[i]=punkte
          note,bestanden=benotung(notenschluessel, punkte)
          if bestanden==True:
            bestanden="ja"
          elif bestanden==False:
            bestanden="nein"
          print(str(matrikelnummer) +"\t" +"\t" +  str(punkte )+"\t" + str(note) + "\t" + str(bestanden))




    
        
else:
        print("Fehler: ungültiger Notenschlüssel")
        print("Ende")
        


