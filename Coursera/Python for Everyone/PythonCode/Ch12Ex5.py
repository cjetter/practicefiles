'''Ch12Ex5: Advanced) Change the socket program so that it only shows data after the headers 
and a blank line have been received. Remember that recv is receiving characters (newlines and all), not lines.
'''
import socket

urlstr = input('Please enter a URL like http://data.pr4e.org: ')
try:
    urlstr = urlstr.strip()
    hoststr = urlstr.split('/')
    host = hoststr[2]
    port = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))
except:
    print('The URL was incorrectly entered or does not exist. Please try again.')
    quit()
cmd = 'GET '+urlstr+' HTTP/1.1\r\nHost: '+host+'\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)
datastream = ''
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    datastream = datastream + str(data.decode())
mysock.close()
pos = datastream.find('\r\n\r\n')
#print(pos)
#print(datastream[:pos])
#print('##########'*8)
print(datastream[pos+4:])