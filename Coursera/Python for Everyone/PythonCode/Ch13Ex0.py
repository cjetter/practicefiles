'''Ch13 : XML ElementTree problem

HOW CAN YOU PULL XML DATA FROM THE WEB?

'''

import xml.etree.ElementTree as ET
import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'w3schools.com'
port = 80
mysock.connect((host,port))
cmd = 'GET https://www.w3schools.com/xml/simplexsl.xml HTTP/1.0\n\n'.encode()
mysock.send(cmd)

datafull = ''

while True:
    data = mysock.recv(4096)
    if len(data) < 0: break
    datafull = datafull + data.decode()
mysock.close()

print(datafull)

tree = ET.fromstring(datafull)
print('Name:', tree.find('name').text)