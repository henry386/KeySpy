from time import sleep
import socket
from datetime import datetime

while True:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("Server: ", ip_address + " " + hostname)

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("127.0.0.1", 9989))

    # The 10 is the maximum number of connections.
    serversocket.listen(10)
    connection, address = serversocket.accept()

    while True:
        try:
            data = connection.recv(1024).decode()
            if len(data) > 0:
                print(data)
                f = open("messagelog.txt", "a+")
                f.write(data + "\n")
                f.close()
        except ConnectionResetError:
            break
