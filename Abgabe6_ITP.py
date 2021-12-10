def batch_bewertung(schluessel, punktzahl):
    if(schluessel == 1 or schluessel == 2 or schluessel == 3):
        if(schluessel == 1):
            if(punktzahl >= 86):
                note = 1
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 82):
                note = 1.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 78):
                note = 1.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 74):
                note = 2.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 70):
                note = 2.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 66):
                note = 2.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 62):
                note = 3.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 58):
                note = 3.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 54):
                note = 3.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 50):
                note = 4.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl < 50):
                note = 5.0
                bestanden = "nein"
                return [note, bestanden]
        elif(schluessel == 2):
            if(punktzahl >= 95):
                note = 1.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 90):
                note = 1.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 85):
                note = 1.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 80):
                note = 2.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 75):
                note = 2.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 70):
                note = 2.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 65):
                note = 3.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 60):
                note = 3.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 55):
                note = 3.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 50):
                note = 4.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl < 50):
                note = 5.0
                bestanden = "nein"
                return [note, bestanden]
        else:
            if(punktzahl >= 85):
                note = 1.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 80):
                note = 1.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 75):
                note = 1.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 70):
                note = 2.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 65):
                note = 2.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 60):
                note = 2.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 55):
                note = 3.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 50):
                note = 3.3
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 45):
                note = 3.7
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl >= 40):
                note = 4.0
                bestanden = "ja"
                return [note, bestanden]
            elif(punktzahl < 40):
                note = 5.0
                bestanden = "nein"
                return [note, bestanden]

klausurenBatch = []
notenschluessel = int(input("Bitte Notenschluessel eingeben, nach dem Klausuren bewertet werden sollen: "))

if(notenschluessel == 1 or notenschluessel == 2 or notenschluessel == 3 ):
    eintragen = True
    while(eintragen):                           
        matrikelnummer = int(input(("Bitte Matrikelnummer eingeben: "))
        punkte = int(input("Bitte geben Sie die erreichte punktzahl ein: "))
        klausurenBatch.append[matrikelnummer, punkte]
        weiteresErgebnis = input("Möchten Sie ein weiteres Ergebnis eintragen?")
        if(weiteresErgebnis == "ja"):
            eintragen == True
        elif(weiteresErgebnis == "ja"):
            eintragen == False
    if(len(klausurenBatch) > 0):
          print("Mtr.\t\tPunkte\tNote\tBestanden\n")
          for ergebnis in klausurenBatch:
              noteBestanden = batch_bewertung(ergebnis[0],ergebnis[1])
              print(f"{ergebnis[0]}\t\t{ergebnis[1]}\t{noteBestanden[0]}\t{noteBestanden[1]}")
else:
    print("Ungültiger Notenschluessel!", end=" ")

print("Programm wird beendet.")
