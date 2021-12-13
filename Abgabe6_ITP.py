def benotung(schluessel, punktzahl):
    if(schluessel == 1 or schluessel == 2 or schluessel == 3):
        if(schluessel == 1):
            if(punktzahl >= 86):
                note = 1.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 82):
                note = 1.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 78):
                note = 1.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 74):
                note = 2.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 70):
                note = 2.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 66):
                note = 2.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 62):
                note = 3.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 58):
                note = 3.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 54):
                note = 3.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 50):
                note = 4.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl < 50):
                note = 5.0
                bestanden = "nein"
                return note, bestanden
        elif(schluessel == 2):
            if(punktzahl >= 95):
                note = 1.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 90):
                note = 1.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 85):
                note = 1.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 80):
                note = 2.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 75):
                note = 2.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 70):
                note = 2.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 65):
                note = 3.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 60):
                note = 3.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 55):
                note = 3.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 50):
                note = 4.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl < 50):
                note = 5.0
                bestanden = "nein"
                return note, bestanden
        else:
            if(punktzahl >= 85):
                note = 1.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 80):
                note = 1.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 75):
                note = 1.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 70):
                note = 2.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 65):
                note = 2.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 60):
                note = 2.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 55):
                note = 3.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 50):
                note = 3.3
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 45):
                note = 3.7
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl >= 40):
                note = 4.0
                bestanden = "ja"
                return note, bestanden
            elif(punktzahl < 40):
                note = 5.0
                bestanden = "nein"
                return note, bestanden

klausuren = []

notenschlüssel = int(input("Notenschlüssel: "))
if(notenschlüssel == 1 or notenschlüssel == 2 or notenschlüssel == 3):
    bewerten = True
    while bewerten:
        matrikelnummer = int(input("Matrikelnummer: "))
        punkte = float(input("erreichte Punktzahl: "))
        note, bestanden = benotung(notenschlüssel, punkte)
        klausuren.append([matrikelnummer, punkte, note, bestanden])
        neuer_eintrag = input("Möchten Sie einen neuen Eintrag erstellen? ")
        if(neuer_eintrag != "ja"):
            break
    print("Matrikelnummer\t\tPunkte\tNote\tBestanden")
    for klausur in klausuren:
        print(f"{klausur[0]}\t\t\t{klausur[1]}\t{klausur[2]}\t\t{klausur[3]}")
else: 
    print("Ungültiger Notenschlüssel. Programm beendet.")