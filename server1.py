import socket
import sys
import ipgetter

hostname=socket.gethostname()
host=socket.gethostbyname(hostname)
wan=ipgetter.myip()
port=int(sys.argv[1])

print ("Your ip address is: " + wan)
print ("Connecting on port: "+ str(port))


s=socket.socket()
s.bind((host,port))

s.listen(5)

c,addr=s.accept()

print("The Connected Device" + str(addr))


while True:

    data=c.recv(1024)

    if not data:
        break
    print ("Client Send: " +(data).decode())

    message=input("-->").encode()
    c.send(message)
c.close()
