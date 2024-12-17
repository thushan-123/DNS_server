class Question():
    
    def __init__(self,bytearray,qtype,qclass):
        self.bytearray = bytearray
        self.qtype = qtype
        self.qclass = qclass
        
    def flags_to_byte(self):
        val_ = bytearray[0] + bytearray[bytearray[0] + 1] + 3   # Filter -> \x07example\x03com\x00 
        print(val_)
        bytearray = bytearray[:val_]
          
        print(bytearray)
        
        hex_val_ = [f"{i:02x}" for i in bytearray]  # Convert to hex value and append 
        hex_str = " ".join(hex_val_)
        
        
            
            
'''
    b'\x07example\x03com\x00\x00\x01\x00\x01\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'
    filter -> \x07example\x03com\x00
    example.com    -> 07 65 78 61 6d 70 6c 65 03 63 6f 6d 00  terminate
'''

q = Question(b'\x07example\x03com\x00\x00\x01\x00\x01\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00')
q.flags_to_byte


