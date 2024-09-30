

import socket

HOST = '127.0.0.1'
PORT = 23325


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    print(f"I am listening on port {PORT}")

    connection, client_address = server_socket.accept()

    print(f"Got a connection from {client_address}")
    while True:
        data = connection.recv(1024)
        print(f"Received {data.decode('UTF-8')}")

        message = f"I received client's message: {data}, \nThank you!"

        connection.send(message.encode('UTF-8'))

