import struct

class Question:
    def __init__(self, raw_data):
        self.name, self.qtype, self.qclass = self.parse_question(raw_data)

    def parse_question(self, data):
        name = []
        i = 0
        while data[i] != 0:  # Parsing the domain name
            length = data[i]
            i += 1
            name.append(data[i:i+length].decode())
            i += length
        domain_name = ".".join(name)
        qtype, qclass = struct.unpack("!HH", data[i+1:i+5])  # QTYPE and QCLASS (next 4 bytes)
        return domain_name, qtype, qclass

    def __str__(self):
        return f"Name: {self.name}, Type: {self.qtype}, Class: {self.qclass}" 
            
            
'''
    b'\x07example\x03com\x00\x00\x01\x00\x01\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'
    filter -> \x07example\x03com\x00
    example.com    -> 07 65 78 61 6d 70 6c 65 03 63 6f 6d 00  terminate
'''

# q = Question(b'\x07example\x03com\x00\x00\x01\x00\x01\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00')
# q.flags_to_byte


