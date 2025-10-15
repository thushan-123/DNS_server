'''
    Header Section

    ID -> 16 bit
    QR -> 1bit | OPCODE -> 4bit | AA -> 1bit | TC -> 1bit | RD -> 1bit | RA -> 1bit | Z -> 3bit | RCODE -> 4bit
    NSCOUNT -> 16bit
    QDCOUNT -> 16bit
    ANCOUNT -> 16bit
    ARCOUNT -> 16bit

'''


class Header:
    def __init__(
        self,
        id,
        qr=0,
        opcode=0,
        aa=0,
        tc=0,
        rd=0,
        ra=1,
        z=0,
        rcode=0,
        ns_count=0,
        qd_count=0,
        anc_count=0,
        ar_count=0
    ):
        self.id = id
        self.qr = qr
        self.opcode = opcode
        self.aa =aa
        self.tc = tc,
        self.rd = rd,
        self.ra = ra,
        self.z = z,
        self.rcode = rcode,
        self.ns_count = ns_count,
        self.qd_count = qd_count,
        self.anc_count = anc_count,
        self.ar_count = ar_count

    def flags_convert_byte(self):
        id_flag = (
            (self.qr << 15) |
            (self.opcode << 11) |
            (self.aa << 10) |
            (self.tc << 9) |
            (self.rd << 8) |
            (self.ra << 7) |
            (self.z << 4) |
            (self.rcode << 0)
        )  # create the 16bit ID

        # create header
        header = (
                self.id.to_bytes(2, "big") +
                id_flag.to_bytes(2, 'big') +
                self.qd_count.to_bytes(2, 'big') +
                self.anc_count.to_bytes(2, 'big') +
                self.ns_count.to_bytes(2, 'big') +
                self.ar_count.to_bytes(2, 'big')
        )

        return header