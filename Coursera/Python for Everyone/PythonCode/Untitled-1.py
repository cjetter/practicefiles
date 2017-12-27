import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.superselectos.com/Tienda/Catalogo/carnes?categoria=272') 
for line in fhand:
    print(line.decode().strip())