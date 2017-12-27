'''Ch12Ex4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document 
and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. 
Test your program on several small web pages as well as some larger web pages.
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

urlstr = input('Please enter a URL like http://data.pr4e.org: ')
try:
    req = urllib.request.Request(urlstr, headers={'User-Agent': 'Mozilla/5.0'})
    fhand = urllib.request.urlopen(req).read()
except:
    print('The URL was incorrectly entered or does not exist. Please try again.')
    quit()
counter = 0
soup = BeautifulSoup(fhand,'lxml')
tags = soup('head')
for tag in tags:
    counter +=1

print('Paragraph tag count: ',counter)