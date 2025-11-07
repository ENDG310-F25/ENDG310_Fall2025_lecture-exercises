import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect( ('data.pr4e.org', 80) )

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) 
    print(len(data))
    if (len(data) < 1):
        break
    print(data.decode(),end='') 
mysock.close()


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 
print("\nNot using a socecket\n")
for line in fhand:
    print(line.decode().strip())

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm') 
for line in fhand:
    print(line.decode().strip())
