def hamming_encode(data):
    data = list(map(int, data))
    
    # Positions: p1 p2 d1 p4 d2 d3 d4
    encoded = [0]*7
    encoded[2] = data[0]
    encoded[4] = data[1]
    encoded[5] = data[2]
    encoded[6] = data[3]
    
    # parity bits
    encoded[0] = encoded[2] ^ encoded[4] ^ encoded[6]
    encoded[1] = encoded[2] ^ encoded[5] ^ encoded[6]
    encoded[3] = encoded[4] ^ encoded[5] ^ encoded[6]
    
    return ''.join(map(str, encoded))

def hamming_decode(received):
    r = list(map(int, received))
    
    p1 = r[0] ^ r[2] ^ r[4] ^ r[6]
    p2 = r[1] ^ r[2] ^ r[5] ^ r[6]
    p4 = r[3] ^ r[4] ^ r[5] ^ r[6]
    
    error_pos = p1 + (p2 << 1) + (p4 << 2)
    
    if error_pos != 0:
        print("Error at position:", error_pos)
        r[error_pos - 1] ^= 1  # correct it
    
    return ''.join(map(str, r))

# Encode
data = "1011"
encoded = hamming_encode(data)
print("Encoded:", encoded)

# Introduce error
received = list(encoded)
received[3] = '1' if received[3]=='0' else '0'
received = ''.join(received)

print("Received with error:", received)

# Decode and correct
corrected = hamming_decode(received)
print("Corrected:", corrected)