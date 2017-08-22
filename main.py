import socket, sys
from threading import Thread

def listener(port=4444,numOfCons = 5):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), port))
    serversocket.listen(numOfCons)
    return serversocket

def sender(ip, port = 4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    return s

def listen(socket,size):
    msg = socket.recv(size)
    print(msg.decode('ascii'))

def send(socket):
    msg = input()
    socket.send(msg.encode('ascii'))

if __name__ == "__main__":
    while True:
        print("Host connection or join connection (h/j)\n")
        choice = input()
        if choice[0].lower() == 'h':
            port = input("Port: ")
            serversocket = listener(port=int(port))
            break
        elif choice[0].lower() == 'j':
            ip = input("ip: ")
            port = input("Port: ")
            s = sender(ip,int(port))
            break
        else:
            print("invalid selection type 'h' or 'j'")

    if choice[0].lower() == 'h':
        (clientsocket, address) = serversocket.accept()
        print(clientsocket, address)
        clientsocket.send("Connection received".encode('ascii'))
        s = clientsocket

    while True:
        Thread(target = listen(s,2048)).start()
        Thread(target = send(s)).start()

