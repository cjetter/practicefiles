'''Ch13: JSON, Google Geocoding API'''

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address)<1: break
    urlext = urllib.parse.urlencode({'address':address})
    print(urlext)
    url = serviceurl+urlext
    print('Retrieving URL: ',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),' characters')
    print(data)
    print(type(data))
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print("========Failure to Retrieve=========")
        print(data)
        continue
    xx = json.dumps(js, indent=4)
    print(xx)
    print(type(xx))

    print(js)
    print(type(js))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    quit()