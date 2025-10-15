import socket


def handle_client(udp_socket: socket.socket, buffer):
    pass

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

            res = b"hello"
            udp_socket.sendto(res, addr)
        except Exception as e:
            print(f"Err : {e}")


if __name__ == "__main__":
    main()