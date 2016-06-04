import googlemaps, sys
from datetime import datetime

key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def finddist(source, destination, mod):
    gmaps = googlemaps.Client(key = key)
    now = datetime.now()
    directions_result = gmaps.directions(source, destination, mode = mod,departure_time = now)
    for map1 in directions_result:
        overall_stats = map1['legs']
        for dimensions in overall_stats:
            distance = dimensions['distance']
            return [distance['text']]

def findtime(source, destination, mod):
      gmaps = googlemaps.Client(key = key)
      now = datetime.now()
      directions_result = gmaps.directions(source, destination, mode = mod,departure_time = now)
      for map1 in directions_result:
            overall_stats = map1['legs']
            for dimensions in overall_stats:
                   duration = dimensions['duration']
                   return [duration['text']]

source = str(input("Enter source name : "))
destination = str(input("Enter destination name : "))
print("Mode of travelling : ")
print("1. Walking")
print("2. Driving")
print("3. Transit")
try:
    x = int(input("Select Index : "))
except:
    print("Invalid Option. Terminating !!!")
    sys.exit(0)
if(x >= 1 and x<= 3):
    if(x == 1):
        mod = "walking"
    elif(x == 2):
        mod = "driving"
    else:
        mod = "transit"
else:
    sys.exit(0)
dist = finddist(source,destination,mod)
time = findtime(source,destination,mod)
print("Estimated driving distance between the places : ",str(dist))
print("Estimated time of travel : ",str(time))
