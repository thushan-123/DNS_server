class Question():
    
    def __init__(self,bytearray):
        val_ = bytearray[0] + bytearray[bytearray[0] + 1] + 3 # filter -> \x07example\x03com\x00 
        print(val_)
        
        bytearray = bytearray[:val_]
         # Convert to hex value and append  
        print(bytearray)
        
        hex_val_ = [f"{i:02x}" for i in bytearray]
        hex_str = " ".join(hex_val_)
        return hex_str
            
            
'''
    b'\x07example\x03com\x00\x00\x01\x00\x01\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'
    filter -> \x07example\x03com\x00
    example.com    -> 07 65 78 61 6d 70 6c 65 03 63 6f 6d 00  terminate
'''


