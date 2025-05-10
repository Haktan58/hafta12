# hafta12 import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

well_known_port = 8881
sock.bind(('', well_known_port))

sock.listen(5)

try:
    while True:

        newSocket, address = sock.accept()
        print("Connected from", address)

        while True:

            receivedData = newSocket.recv(1024)
            if not receivedData:
                break


            newSocket.send(receivedData)


        newSocket.close()
        print("Disconnected from", address)

finally:

    sock.close()
