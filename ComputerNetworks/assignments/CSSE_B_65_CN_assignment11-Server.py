# import socket

# SERVER_IP = "0.0.0.0"
# PORT = 5005
# BUFFER_SIZE = 1024

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((SERVER_IP, PORT))

# print("Server ready to receive file...")

# file_data = {}
# file_name = "received_file"
# expected_packets = None

# while True:
#     packet, addr = sock.recvfrom(BUFFER_SIZE + 10)

#     packet_type = packet[0]

#     # START packet
#     if packet_type == 0:
#         meta = packet[1:].decode()
#         file_name, file_size = meta.split("|")
#         file_size = int(file_size)

#         print(f"Receiving file: {file_name} ({file_size} bytes)")

#         sock.sendto(b"START_ACK", addr)

#     # DATA packet
#     elif packet_type == 1:
#         seq_no = int.from_bytes(packet[1:5], 'big')
#         data = packet[5:]

#         file_data[seq_no] = data

#         print(f"Received chunk {seq_no}")

#         # Send ACK
#         sock.sendto(seq_no.to_bytes(4, 'big'), addr)

#     # END packet
#     elif packet_type == 2:
#         print("All packets received. Reconstructing file...")

#         with open("downloaded_" + file_name, "wb") as f:
#             for i in sorted(file_data.keys()):
#                 f.write(file_data[i])

#         print(f"File saved as downloaded_{file_name}")
#         sock.sendto(b"END_ACK", addr)
#         break


import socket

SERVER_IP = "0.0.0.0"
PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print("Receiver ready...")

received_data = {}
expected_seq = 0

while True:
    packet, addr = sock.recvfrom(BUFFER_SIZE + 4)

    seq_no = int.from_bytes(packet[:4], 'big')
    data = packet[4:]

    print(f"Received packet {seq_no}")

    received_data[seq_no] = data

    sock.sendto(seq_no.to_bytes(4, 'big'), addr)

    if len(data) == 0:
        break

# Reassemble file
with open("received_file", "wb") as f:
    for i in sorted(received_data.keys()):
        f.write(received_data[i])

print("File received successfully.")