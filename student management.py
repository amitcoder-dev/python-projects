# simple server example
import socket

server = socket.socket()
server.bind(('localhost',12345))
server.listen(1)

client, addr = server.accept()
print("Connected:", addr)

while True:
    msg = client.recv(1024).decode()
    print("Client:", msg)
    client.send("Received".encode())