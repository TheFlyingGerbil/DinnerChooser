import googlemaps
from datetime import datetime

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close()
gmaps = googlemaps.Client(key=api_key)

now = datetime.now()
#directions_result = gmaps.directions('47.41711, -122.17986','47.44439, -122.19786', avoid = 'ferries', departure_time=now)

result = gmaps.distance_matrix('47.41711, -122.17986','47.44439, -122.19786', mode='driving')["rows"][0]["elements"][0]["distance"]["value"]

#print(directions_result[0]['legs'][0]['distance']['text'])
#print(directions_result[0]['legs'][0]['duration']['text'])