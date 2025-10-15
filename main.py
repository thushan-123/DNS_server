import socket
from typing import Any

from header.Header import Header

def handle_client(udp_socket: socket.socket, address: Any, buffer):
    transaction_id = buffer[:2]
    question_data = buffer[12:]
    qd_count = buffer[4:6]
    header_f = buffer[2:12]



    h = Header(
        id=int.from_bytes(transaction_id, 'big'),
        qr=1,
        opcode=0,
        aa=0,
        tc=0,
        rd=0,
        ra=0,
        z=0,
        rcode=0,
        qd_count=int.from_bytes(qd_count, 'big'),
        ns_count=0,
        an_count=0,
        ar_count=0
    )  # create header object

    res = b""
    res += h.flags_convert_byte()

    udp_socket.sendto(res,address)


def main():
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    ) # crate  udp socket

    udp_socket.bind(("127.0.0.1", 2053)) # bind ip and port

    print("DNS Server running on 127.0.0.1:2053")

    while True:
        try:
            buffer , addr = udp_socket.recvfrom(1024) #buffer size 1024 bytes

            print(buffer)

            handle_client(udp_socket,addr,buffer)
        except Exception as e:
            print(f"Err : {e}")


if __name__ == "__main__":
    main()