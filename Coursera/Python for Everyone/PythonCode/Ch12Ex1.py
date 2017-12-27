'''Ch12Ex1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
You can use split(’/’) to break the URL into its component parts so you can extract the host name for the socket connect call. 
Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

#### HOW DO YOU HANDLE HTTP VS HTTPS?
**** WHAT IS THE DIFFERENCE BETWEEN HANDLING HTTP 1.0 AND 1.1?

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
cmd = 'GET '+urlstr+' HTTP  /1.1\r\nHost: '+host+'\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()