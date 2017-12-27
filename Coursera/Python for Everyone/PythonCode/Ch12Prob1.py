'''Ch12 Online Problem1: You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
'''
import urllib
from BeautifulSoup import *

urlstr = raw_input('Please enter a URL like http://data.pr4e.org: ')
try:
    fhand = urllib.urlopen(urlstr).read()
    soup = BeautifulSoup(fhand)
except:
    print 'The URL was incorrectly entered or does not exist. Please try again.'
    quit()

total = 0
tags = soup('span')
for tag in tags:
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    total = total + int(tag.contents[0])
    #print 'Attrs:',tag.attrs
print 'Sum total: ',total