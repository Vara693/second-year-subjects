# import socket
# import os
# import time

# SERVER_IP = "127.0.0.1"
# PORT = 5005
# BUFFER_SIZE = 1024
# TIMEOUT = 1

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.settimeout(TIMEOUT)

# file_path = "path_of_file_to_send"

# file_name = os.path.basename(file_path)
# file_size = os.path.getsize(file_path)

# # --- SEND START ---
# start_msg = f"{file_name}|{file_size}".encode()
# sock.sendto(bytes([0]) + start_msg, (SERVER_IP, PORT))

# sock.recvfrom(1024)
# print("Start acknowledged")

# # --- SEND FILE DATA ---
# seq_no = 0

# with open(file_path, "rb") as f:
#     while True:
#         data = f.read(BUFFER_SIZE)
#         if not data:
#             break

#         packet = bytes([1]) + seq_no.to_bytes(4, 'big') + data

#         while True:
#             sock.sendto(packet, (SERVER_IP, PORT))

#             try:
#                 ack, _ = sock.recvfrom(4)
#                 ack_no = int.from_bytes(ack, 'big')

#                 if ack_no == seq_no:
#                     print(f"ACK {seq_no}")
#                     break
#             except socket.timeout:
#                 print(f"Resending {seq_no}")

#         seq_no += 1

# # --- SEND END ---
# sock.sendto(bytes([2]), (SERVER_IP, PORT))
# sock.recvfrom(1024)

# print("File transfer complete")



import socket
import time

SERVER_IP = "127.0.0.1"
PORT = 5005
BUFFER_SIZE = 1024
TIMEOUT = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

seq_no = 0

with open("path_to_the_file", "rb") as f:
    while True:
        data = f.read(BUFFER_SIZE)
        packet = seq_no.to_bytes(4, 'big') + data

        while True:
            sock.sendto(packet, (SERVER_IP, PORT))

            try:
                ack, _ = sock.recvfrom(4)
                ack_no = int.from_bytes(ack, 'big')

                if ack_no == seq_no:
                    print(f"ACK received for {seq_no}")
                    break
            except socket.timeout:
                print(f"Timeout, retransmitting {seq_no}")

        if not data:
            break

        seq_no += 1

print("File sent successfully.")