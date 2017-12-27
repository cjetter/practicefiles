'''Ch13:Pr3 JSON, Google Geocoding API

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. 
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

'''
import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print("========Failure to Retrieve=========")
        print(data)
        continue
    
    placeid = js["results"][0]["place_id"]
    print(placeid)
    quit()