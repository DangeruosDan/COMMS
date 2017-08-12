import socket, sys

def listener(port=4444,numOfCons = 3):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), port))
    serversocket.listen(numOfCons)
    return serversocket

def sender(ip = "192.168.1.1", port = 4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    return s

if __name__ == "__main__":
    serversocket = listener()
    s = sender()
    while True:
        (clientsocket, address) = serversocket.accept()
        print(clientsocket, address)
