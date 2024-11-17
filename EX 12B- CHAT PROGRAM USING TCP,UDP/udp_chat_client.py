import socket

def udp_chat_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("You: darshita ")
        if message.lower() == 'exit':
            break
        client_socket.sendto(message.encode('utf-8'), (host, port))
        
        response, _ = client_socket.recvfrom(1024)
        print(f"Server: {response.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    udp_chat_client()
