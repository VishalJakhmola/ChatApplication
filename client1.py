import socket
import sys
def main():
    
    ip=sys.argv[1]
    port=sys.argv[2]

    s=socket.socket()
    s.connect((ip,port))

    message=input("-->").encode()

    while(message!="bye"):
        s.send(message)
        data=s.recv(1024)
        print("Message from server:"+data.decode())

    s.close()

if__name__=='__main__':
    main()






