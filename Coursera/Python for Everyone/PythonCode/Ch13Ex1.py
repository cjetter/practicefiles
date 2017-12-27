'''Ch13Ex1: JSON, Google Geocoding API
Change either the www.py4e.com/code3/geojson.py or www.py4e.com/code3/geoxml.py to print out the two-character country code 
from the retrieved data. Add error checking so your program does not traceback if the country code is not there.
Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.
'''

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address)<1: break
    urlext = urllib.parse.urlencode({'address':address})
    #print(urlext)
    url = serviceurl+urlext
    print('Retrieving URL: ',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print('Retrieved',len(data),' characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print("========Failure to Retrieve=========")
        print(data)
        continue
    #print(json.dumps(js,indent=4))

    mylist = js["results"][0]["address_components"]
    counter=-1
    indexNo = None
    for x in mylist:
        keyterm = x['types'][0]
        counter = counter+1
        if keyterm == 'country':
            indexNo = counter
            break
    try:
        CountryCode = js["results"][0]["address_components"][indexNo]["short_name"]
        print(CountryCode)
    except:
        print('Location is not found within a country.')
    location = js['results'][0]['formatted_address']
    print(location)
    quit()