import random
from socket import *

def main():

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 12001))

    while True:
        
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message.decode())

        if "PING" in message.decode():
            pingrec = f"Reply from {clientAddress}: {message.decode()}"
            serverSocket.sendto(pingrec.encode(), clientAddress)
     
if __name__ == '__main__': 
    main()