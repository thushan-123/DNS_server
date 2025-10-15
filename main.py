import socket


def main():
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    ) # crate  udp socket

    udp_socket.bind(("127.0.0.1", 2053)) # bind ip and port

    while True:
        try:
            buffer , source = udp_socket.recv(1024) #buffer size 1024 bytes
        except Exception as e:
            print(f"Err : {e}")


if __name__ == "__main__":
    main()