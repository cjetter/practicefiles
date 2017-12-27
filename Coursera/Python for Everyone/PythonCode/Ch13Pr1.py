import urllib
import xml.etree.ElementTree as ET

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print('Retrieved',len(data),' characters')
    
    tree = ET.fromstring(data)
    results = tree.findall('comments/comment')
    total = 0
    counter = 0
    for result in results:
        print(result.text)
        #x = result[1].text
        #counter = counter +1
        #total = total + int(x)
    
   # print 'Count: ',counter
    #print 'Sum: ',total
    #quit()