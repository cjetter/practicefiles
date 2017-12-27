import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.superselectos.com/Tienda/Catalogo/carnes?categoria=272&marca=&page=1&tipoEspecial=Ninguno&catEspecial=0#detalleProducto'
fh = urllib.request.urlopen(url, context=ctx)
data = fh.read().decode('utf-8-sig')
#headers = dict(fh.getheaders())
#print(headers)
print(data)
    
#fhand = open('SuperSelectos.txt','w')
#fhand.write(data)
#fhand.close()
#quit()