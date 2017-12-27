'''Ch12 : Http test code'''

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'data.pr4e.org'
mysock.connect((host, 80))
#print(mysock.getsockname())
#print(mysock.family)
#print(mysock.type)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.1\r\nHost: '+host+'\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()