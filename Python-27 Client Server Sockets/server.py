import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 23321


server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

print(f"server is listening to port {SERVER_PORT}")


clients = []
nicknames= []


def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} has disconnected!".encode('utf-8'))
            nicknames.remove(nickname)
            client.close()
            break

def receive_client():
    while True:
        client, address = server_socket.accept()
        print(f"client {address} connected")


        client.send("nickname".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f"client {nickname} connected")
        broadcast(f"{nickname} has connected!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive_client()


