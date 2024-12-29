import socket
import struct

class Answer:
    def generate_answer(self, domain_name, record_type, records):
        """
        Generate DNS Answer Section
        """
        result = b""

        # Pointer to the domain name (use offset to Question Section)
        result += b'\xc0\x0c'  # Offset 12 bytes to point to the Question section

        # Type (2 bytes) -> A Record: 1
        result += struct.pack("!H", record_type)

        # Class (2 bytes) -> IN (Internet): 1
        result += struct.pack("!H", 1)

        # TTL (4 bytes)
        result += struct.pack("!I", 60)

        # Data Length (2 bytes)
        result += struct.pack("!H", 4)  # IPv4 address length is 4 bytes

        # Record Data: Convert IP Address to 4 bytes
        for record in records:
            ip_bytes = bytes(map(int, record.split(".")))  # Convert IP address to byte format
            result += ip_bytes

        return result
