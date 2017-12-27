'''Ch12 Online Proble2: Start at: http://python-data.dr-chuck.net/known_by_Dharam.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: K
'''
import urllib
from BeautifulSoup import *

targetlink = raw_input('Please enter a URL like http://data.pr4e.org: ')
position = int(raw_input('Enter position: '))-1
cycle_count = int(raw_input('Enter number of cycles: '))+1

counter = 0
for x in range(0,(cycle_count-1)):
    counter+=1
    fhand = urllib.urlopen(targetlink).read()
    soup = BeautifulSoup(fhand)
    tags = soup('a')
    targetlink = tags[position]
    targetlink = str(targetlink.get('href', None))
    print targetlink
    if counter == int(cycle_count): break

print '\nTarget link: ',targetlink,'\n'