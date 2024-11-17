import socket
def tcp_echo_client(host='localhost', port=12345, message='Hello, World!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
if __name__ == "__main__":
    tcp_echo_client(message="Hello, darshita!")
