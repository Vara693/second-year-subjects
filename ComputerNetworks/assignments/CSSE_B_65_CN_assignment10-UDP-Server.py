import socket

HOST = '127.0.0.1'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("UDP Server listening...")

while True:
    data, addr = server.recvfrom(1024)
    print(f"Client {addr}: {data.decode()}")
    server.sendto(data, addr)  # Echo back