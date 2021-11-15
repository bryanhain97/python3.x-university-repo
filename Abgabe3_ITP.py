print("Programm um Klausurnote zu bestimmen gestartet.")
print("Es wird anhand des eingegebenen Notenschlüssels (1-3) \n"
      "und ihrer erreichten Punktzahl (0-100) ihre Klausurnote bestimmt.")


notenschlüssel = float(input("Notenschlüssel eingeben (1-3): "))
punktzahl = float(input("Erreichte Punktzahl eingeben: "))
if (notenschlüssel == 1):
    print(f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}")
    if(punktzahl >= 86):
        print("Note: 1.0")
    elif(punktzahl >= 82):
        print("Note: 1.3")
    elif(punktzahl >= 78):
        print("Note: 1.7")
    elif(punktzahl >= 74):
        print("Note: 2.0")
    elif(punktzahl >= 70):
        print("Note: 2.3")
    elif(punktzahl >= 66):
        print("Note: 2.7")
    elif(punktzahl >= 62):
        print("Note: 3.0")
    elif(punktzahl >= 58):
        print("Note: 3.3")
    elif(punktzahl >= 54):
        print("Note: 3.7")
    elif(punktzahl >= 50):
        print("Note: 4.0")
    elif(punktzahl < 50):
        print("Note: 5.0")
    print("Programm erfolgreich beendet.")
elif (notenschlüssel == 2):
    print(f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}")
    if(punktzahl >= 95):
        print("Note: 1.0")
    elif(punktzahl >= 90):
        print("Note: 1.3")
    elif(punktzahl >= 85):
        print("Note: 1.7")
    elif(punktzahl >= 80):
        print("Note: 2.0")
    elif(punktzahl >= 75):
        print("Note: 2.3")
    elif(punktzahl >= 70):
        print("Note: 2.7")
    elif(punktzahl >= 65):
        print("Note: 3.0")
    elif(punktzahl >= 60):
        print("Note: 3.3")
    elif(punktzahl >= 55):
        print("Note: 3.7")
    elif(punktzahl >= 50):
        print("Note: 4.0")
    elif(punktzahl < 50):
        print("Note: 5.0")
    print("Programm erfolgreich beendet.")
elif (notenschlüssel == 3):
    print(f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}")
    if(punktzahl >= 85):
        print("Note: 1.0")
    elif(punktzahl >= 80):
        print("Note: 1.3")
    elif(punktzahl >= 75):
        print("Note: 1.7")
    elif(punktzahl >= 70):
        print("Note: 2.0")
    elif(punktzahl >= 65):
        print("Note: 2.3")
    elif(punktzahl >= 60):
        print("Note: 2.7")
    elif(punktzahl >= 55):
        print("Note: 3.0")
    elif(punktzahl >= 50):
        print("Note: 3.3")
    elif(punktzahl >= 45):
        print("Note: 3.7")
    elif(punktzahl >= 40):
        print("Note: 4.0")
    elif(punktzahl < 40):
        print("Note: 5.0")
    print("Programm erfolgreich beendet.")
else:
    print("Eingabe ungültig. Notenschlüssel (1-3)!")
    print("Programm beendet.")
