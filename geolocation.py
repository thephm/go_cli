"""Experimental helper for fetching the current location via Google Geolocation."""

import requests

def get_location_google(api_key):
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key
    headers = {
        'Content-Type': 'application/json',
    }
    data = {}  # Optionally, include WiFi access points, cell towers, etc.
    try:
        response = requests.post(url, headers=headers, json=data)
        print(response.json()) 
        location_data = response.json()
        latitude = location_data['location']['lat']
        longitude = location_data['location']['lng']
        accuracy = location_data['accuracy']  # meters
        return latitude, longitude, accuracy
    except Exception as e:
        print("Error fetching location from Google API:", e)
        return None

# Use your Google Geolocation API key here
api_key = ''
location = get_location_google(api_key)

if location:
    print(f"Latitude: {location[0]}, Longitude: {location[1]}, Accuracy: {location[2]} meters")
else:
    print("Could not retrieve location.")

