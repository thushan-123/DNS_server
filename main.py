import socket


def main():
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    ) # crate  udp socket

    udp_socket.bind(("127.0.0.1", 2053)) # bind ip and port

    while True:
        try:
            pass
        except Exception as e:
            print(f"Err : {e}")
