'''
    Header Section

    ID -> 16 bit
    QR -> 1bit | OPCODE -> 4bit | AA -> 1bit | TC -> 1bit | RD -> 1bit | RA -> 1bit | Z -> 3bit | RCODE -> 4bit 
    NSCOUNT -> 16bit
    QDCOUNT -> 16bit
    ANCOUNT -> 16bit
    ARCOUNT -> 16bit
    
'''

class Header():
    
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
        
        