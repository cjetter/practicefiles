import urllib
import json

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print('Retrieved',len(data),' characters')
    
    results = json.loads(data)
    results = results['comments']
    total = 0
    counter = 0
    for result in results:
        x = result['count']
        counter = counter +1
        total = total + int(x)
    
    print 'Count: ',counter
    print 'Sum: ',total
    quit()