import socket

LISTENER_IP = str(input('Enter the listeners ip :'))  
LISTENER_PORT = 4444

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LISTENER_IP, LISTENER_PORT))
    server.listen(1)
    print(f"[*] Listening on {LISTENER_IP}:{LISTENER_PORT}...")
    client_socket, addr = server.accept()
    print(f"[*] Connection established from {addr}")
    while True:
        command = input(f"Shell@{addr}> ")
        if command.strip().lower() == 'exit':
            client_socket.send(b'exit')
            client_socket.close()
            break
        client_socket.send(command.encode('utf-8'))
        result = client_socket.recv(4096)
        print(result.decode('utf-8'))

if __name__ == "__main__":
    start_listener()
