def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def crc(data, key):
    key_len = len(key)
    data = data + '0'*(key_len-1)
    tmp = data[:key_len]
    
    for i in range(key_len, len(data)):
        if tmp[0] == '1':
            tmp = xor(key, tmp) + data[i]
        else:
            tmp = xor('0'*key_len, tmp) + data[i]
        tmp = tmp[1:]
    
    return tmp

# Example
data = "1101011011"
key = "10011"

remainder = crc(data, key)
print("CRC:", remainder)

# Receiver check
received = data + remainder
print("Error detected?", crc(received, key) != '0'*(len(key)-1))