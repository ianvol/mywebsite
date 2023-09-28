from django.shortcuts import render
import requests

MAPBOX = settings.MAPBOX

def iss(request):
    iss_json = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
    longitude = float(iss_json["iss_position"]["longitude"])
    latitude = float(iss_json["iss_position"]["latitude"])

    print(longitude)
    
    map_url = f"https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/static/pin-l-circle+ffffff({longitude},{latitude})/{longitude},{latitude},1,0/600x500@2x?access_token={MAPBOX}"

    context = {
        'longitude': longitude,
        'latitude': latitude,
        'map_url': map_url,
    }
    return render(request, 'iss.html', context)


def fetch_iss_data():
    iss_json = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
    longitude = float(iss_json["iss_position"]["longitude"])
    latitude = float(iss_json["iss_position"]["latitude"])
    
    map_url = f"https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/static/pin-l-circle+ffffff({longitude},{latitude})/{longitude},{latitude},1,0/600x500@2x?access_token={MAPBOX}"

    context = {
        'longitude': longitude,
        'latitude': latitude,
        'map_url': map_url,
    }
    return context
