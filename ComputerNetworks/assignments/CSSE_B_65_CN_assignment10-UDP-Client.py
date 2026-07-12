import socket

HOST = '127.0.0.1'
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("You: ")
    client.sendto(msg.encode(), (HOST, PORT))
    
    data, _ = client.recvfrom(1024)
    print("Server:", data.decode())