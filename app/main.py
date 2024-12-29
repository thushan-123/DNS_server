import socket
import struct
from .question import Question
from .header import Header
from .answer import Answer
'''
    test cmd > dig @127.0.0.1 -p 2053 example.com A
'''

def main():
    print("Start DOMAIN NAME SYSTEM SERVER ")
    print("---------------------------------")
    print("Logs from your program will appear here!")

    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))
    
    answer = Answer()
    
    while True:
        try:
            buf, source = udp_socket.recvfrom(512)
            
            print(buf)
            
            transaction_id = buf[:2]
            question_data = buf[12:]
            qdcount = buf[4:6]
            header_flag = buf[2:12]
            
            
            
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
            question = Question(question_data)
    
            response = b""
            
            response += header.flags_to_bytes()
            response += buf[12:12+len(question_data)]
            
            # Generate an answer if the query is for example.com
            if question.name == "example.com" and question.qtype == 1:  # A record
                records = ["93.184.216.34"]  # Example.com IP address
                response += answer.generate_answer(question.name, question.qtype, records)

            print(response)
    
            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break


if __name__ == "__main__":
    main()
