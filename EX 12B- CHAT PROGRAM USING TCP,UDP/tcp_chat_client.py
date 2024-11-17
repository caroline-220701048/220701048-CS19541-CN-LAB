import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Server: {message}")

def tcp_chat_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input("You: darshita ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    tcp_chat_client()
