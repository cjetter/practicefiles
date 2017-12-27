'''Ch12Ex2: Change your socket program so that it counts the number of characters it has received and 
stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document 
and count the total number of characters and display the count of the number of characters at the end of the
document.

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
char = 0
strprint = ''
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    datastream = str(data.decode())
    for x in datastream:
        char +=1
        if char <= 3000:
            strprint = strprint+x
print(strprint)
print('Character count: ',char)
mysock.close()