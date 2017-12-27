
import urllib

html = urllib.urlopen('http://www.py4e.com/book.htm').read()
print(html.decode())
