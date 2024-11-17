import socket

def udp_echo_client(host='localhost', port=12345, message='Hello, World!'):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(message.encode(), (host, port))
        data, _ = client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")
if __name__ == "__main__":
    udp_echo_client(message="Hello, darshita!")
