from numpy import sin, cos, arccos, pi

airports = {
    "Berlin": {
        "lat": 52.365,
        "lon": 13.51,
        "mögliche_zielflughäfen": ("Marrakesch", "Montreal")
    },
    "Marrakesch": {
        "lat": 31.6,
        "lon": -8.025,
        "mögliche_zielflughäfen": ("Berlin", "Lima", "Montreal")
    },
    "Montreal": {
        "lat": 45.67,
        "lon": -74.04,
        "mögliche_zielflughäfen": ("Berlin", "Marrakesch", "Lima", "Ulaanbaatar")
    },
    "Lima": {
        "lat": -12.02,
        "lon": -77.11,
        "mögliche_zielflughäfen": ("Marrakesch", "Montreal")
    },
    "Ulaanbaatar": {
        "lat": 47.85,
        "lon": 106.76,
        "mögliche_zielflughäfen": ("Montreal",)
    }
}

print("Mögliche Startflughäfen:", end=" ")
for i in airports.keys():
    print(i, end=" ")

startflughafen = input("Bitte Startflughafen eingeben: ")
if(startflughafen in airports.keys()):
    mögliche_zielflughäfen = airports[startflughafen]["mögliche_zielflughäfen"]
    print("Zielflughäfen:", end=" ")
    for i in mögliche_zielflughäfen:
        print(i, end=" ")
    zielflughafen = input("\nBitte Zielflughafen eingeben: ")
    alleZielflughäfen = []
    for j in airports.keys():
        for k in airports[j]["mögliche_zielflughäfen"]:
            alleZielflughäfen.append(k)
    alleZielflughäfen = tuple(alleZielflughäfen)
    if(zielflughafen in alleZielflughäfen):
        if(zielflughafen in mögliche_zielflughäfen):
            airport1Lat = airports[startflughafen]["lat"]
            airport1Lon = airports[startflughafen]["lon"]
            airport2Lat = airports[zielflughafen]["lat"]
            airport2Lon = airports[zielflughafen]["lon"]
            orthodrome = arccos(sin(airport1Lat) * sin(airport2Lat) + cos(airport1Lat) * cos(airport2Lat) * cos(abs(airport2Lon - airport1Lon)))
            distanz = round(6371 * orthodrome)
            print(f"Distanz (in km) : {distanz}")
        else:
            print("Eingebener Flughafen wird vom Startflughafen nicht angeflogen!")
    else:
        "Fehler: Der Zielflughafen existiert nicht!"

else:
    print("Unbekannter Flughafen!")