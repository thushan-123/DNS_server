import socket
import struct
from .question import Question
from .header import Header

'''
    test cmd > dig @127.0.0.1 -p 2053 example.com A
'''

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
            question = buf[12:]
            qdcount = buf[4:6]
            print(question)
            
            header = Header(
                        id=int.from_bytes(transaction_id,'big'),
                        qr=1,
                        opcode=0,
                        aa=0,
                        tc=0,
                        rd=0,
                        ra=0,
                        z=0,
                        rcode=0,
                        qdcount=int.from_bytes(qdcount,'big'),
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
