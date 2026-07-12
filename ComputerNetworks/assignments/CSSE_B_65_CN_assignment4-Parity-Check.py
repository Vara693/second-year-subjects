def add_parity(data):
    parity = sum(int(bit) for bit in data) % 2
    return data + str(parity)

def check_parity(data):
    return sum(int(bit) for bit in data) % 2 == 0

# Sender
data = "1011001"
encoded = add_parity(data)
print("Encoded:", encoded)

# Simulate error
received = "1011000"  # one bit flipped
print("Error detected?", not check_parity(received))