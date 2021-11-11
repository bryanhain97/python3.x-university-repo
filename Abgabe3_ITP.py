print("Programm um Klausurnote zu bestimmen gestartet.")
print("Es wird anhand des eingegebenen Notenschlüssels (1-3) \n"
      "und ihrer erreichten Punktzahl ihre Klausurnote bestimmt.")
notenschlüssel = float(input("Notenschlüssel eingeben (1-3): "))

if (notenschlüssel == 1):
    punktzahl = float(input("Erreichte Punktzahl eingeben: "))
    if(punktzahl >= 86):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.0")
    elif(punktzahl >= 82):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.3")
    elif(punktzahl >= 78):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.7")
    elif(punktzahl >= 74):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.0")
    elif(punktzahl >= 70):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.3")
    elif(punktzahl >= 66):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.7")
    elif(punktzahl >= 62):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.0")
    elif(punktzahl >= 58):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.3")
    elif(punktzahl >= 54):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.7")
    elif(punktzahl >= 50):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 4.0")
    elif(punktzahl < 50):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 5.0")
    print("Programm erfolgreich beendet.")
elif(notenschlüssel == 2):
    punktzahl = float(input("Erreichte Punktzahl eingeben: "))
    if(punktzahl >= 95):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.0")
    elif(punktzahl >= 90):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.3")
    elif(punktzahl >= 85):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.7")
    elif(punktzahl >= 80):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.0")
    elif(punktzahl >= 75):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.3")
    elif(punktzahl >= 70):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.7")
    elif(punktzahl >= 65):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.0")
    elif(punktzahl >= 60):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.3")
    elif(punktzahl >= 55):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.7")
    elif(punktzahl >= 50):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 4.0")
    elif(punktzahl < 50):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 5.0")
    print("Programm erfolgreich beendet.")
elif(notenschlüssel == 3):
    punktzahl = float(input("Erreichte Punktzahl eingeben: "))
    if(punktzahl >= 85):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.0")
    elif(punktzahl >= 80):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.3")
    elif(punktzahl >= 75):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 1.7")
    elif(punktzahl >= 70):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.0")
    elif(punktzahl >= 65):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.3")
    elif(punktzahl >= 60):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 2.7")
    elif(punktzahl >= 55):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.0")
    elif(punktzahl >= 50):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.3")
    elif(punktzahl >= 45):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 3.7")
    elif(punktzahl >= 40):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 4.0")
    elif(punktzahl < 40):
        print(
            f"Notenschlüssel: {notenschlüssel}\nPunktzahl: {punktzahl}\nNote: 5.0")
    print("Programm erfolgreich beendet.")
else:
    print("Eingabe ungültig. Notenschlüssel (1-3)!")
    print("Programm beendet.")
