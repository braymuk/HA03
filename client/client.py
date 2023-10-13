import socket
import threading
import os

def send_message(client_socket, message):
    client_socket.send(message.encode())

def send_file(client_socket, filename):
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

def main():
    host = 'localhost'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    command = ""
    message_thread = threading.Thread(target=send_message, args=(client, command))
    message_thread.start()

    while True:
        command = input()
        if command.startswith("/file"):
            file_path = command[6:]
            send_file(client, file_path)
        else:
            send_message(client, command)
            

if __name__ == '__main__':
    main()
