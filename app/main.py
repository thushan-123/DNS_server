import socket
import struct

'''
    ID -> 16 bit
    QR -> 1bit | OPCODE -> 4bit | AA -> 1bit | TC -> 1bit | RD -> 1bit | RA -> 1bit | Z -> 3bit | RCODE -> 4bit 
    NSCOUNT -> 16bit
    QDCOUNT -> 16bit
    ANCOUNT -> 16bit
    ARCOUNT -> 16bit
    
    test cmd > dig @127.0.0.1 -p 2053 example.com A
'''

class init_header():
    
    def __init__(
        self,
        id,
        qr=0,
        opcode=0,
        aa=0,
        tc=0,
        rd=0,
        ra=0,
        z=0,
        rcode=0,
        qdcount=0,
        nscount=0,
        ancount=0,
        arcount=0,
                 ):
        self.id = id
        self.qr = qr
        self.opcode = opcode
        self.aa = aa
        self.tc = tc
        self.rd = rd
        self.ra = ra
        self.z = z
        self.rcode = rcode
        self.qdcount = qdcount
        self.ancount = ancount
        self.nscount = nscount 
        self.arcount = arcount
        
    def flags_to_bytes(self):
        flg = (
            ( self.qr << 15 ) |
            (self.opcode << 11) |
            (self.aa << 10) |
            (self.tc << 9) |
            (self.rd << 8) |
            (self.ra << 7) |
            (self.z << 4) |
            (self.rcode << 0) 
        )
        # create the header 
        header = (
            self.id.to_bytes(2,"big") +
            flg.to_bytes(2,'big') +
            self.qdcount.to_bytes(2,'big') +
            self.ancount.to_bytes(2,'big') +
            self.nscount.to_bytes(2,'big') +
            self.arcount.to_bytes(2,'big')
        )
        
        return header
        
        

            

        


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))
    
    while True:
        try:
            buf, source = udp_socket.recvfrom(512)
            
            print(buf)
            
            transaction_id = buf[:2]
            
            header = init_header(
                        id=int.from_bytes(transaction_id,'big'),
                        qr=1,
                        opcode=0,
                        aa=0,
                        tc=0,
                        rd=0,
                        ra=0,
                        z=0,
                        rcode=0,
                        qdcount=0,
                        nscount=0,
                        ancount=0,
                        arcount=0
                    )
    
            response = b""
            
            response = header.flags_to_bytes()
            print(response)
    
            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break


if __name__ == "__main__":
    main()
