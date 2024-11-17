import socket

def tcp_echo_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Echo Server running on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"Connected by {addr}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    client_socket.sendall(data)

if __name__ == "__main__":
    tcp_echo_server()
