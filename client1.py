import socket
import sys

    
ip=str(sys.argv[1])
port=int(sys.argv[2])

s=socket.socket()
s.connect((ip,port))

message=input("-->").encode()

while(message!="bye"):
    s.send(message)
    data=s.recv(1024)
    print("Message from server:"+data.decode())
    message=input("--> :").encode("utf-8")

s.close()





