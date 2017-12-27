'''Ch12Ex3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
'''
import urllib.request, urllib.parse, urllib.error

urlstr = input('Please enter a URL like http://data.pr4e.org: ')
try:
    req = urllib.request.Request(urlstr, headers={'User-Agent': 'Mozilla/5.0'})
    fhand = urllib.request.urlopen(req).read()
except:
    print('The URL was incorrectly entered or does not exist. Please try again.')
    quit()
counter = 0
strprint = ''
fhand = fhand.decode()

for line in fhand:
    counter +=1
    if counter <= 3000:
        strprint = strprint+str(line)
print(strprint)
print('Character count: ',counter)