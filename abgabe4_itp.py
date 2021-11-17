from numpy import sin, cos, arccos, pi

airports = {
    "Berlin": {
        "lat": 52.365,
        "lon": 13.51,
        "mögliche_zielflughäfen": ["Marrakesch", "Montreal"]
    },
    "Marrakesch": {
        "lat": 31.6,
        "lon": -8.025,
        "mögliche_zielflughäfen": ["Berlin", "Lima", "Montreal"]
    },
    "Montreal": {
        "lat": 45.67,
        "lon": -74.04,
        "mögliche_zielflughäfen": ["Berlin", "Marrakesch", "Lima", "Ulaanbaatar"]
    },
    "Lima": {
        "lat": -12.02,
        "lon": -77.11,
        "mögliche_zielflughäfen": ["Marrakesch", "Montreal"]
    },
    "Ulaanbaatar": {
        "lat": 47.85,
        "lon": 106.76,
        "mögliche_zielflughäfen": ["Montreal"]
    }
}

