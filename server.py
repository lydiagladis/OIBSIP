import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

clients = []


def get_time():
    return datetime.now().strftime("%H:%M")


def handle_client(client):
    try:
        name = client.recv(1024).decode()
        clients.append((client, name))

        print(name, "connected.")

        # Tell the other client that someone joined
        for other_client, other_name in clients:
            if other_client != client:
                message = f"[{get_time()}] {name} joined the chat."
                other_client.send(message.encode())

        while True:
            message = client.recv(1024).decode()

            if not message:
                break

            message = f"[{get_time()}] {name}: {message}"

            print(message)

            # Send message to the other client
            for other_client, other_name in clients:
                if other_client != client:
                    other_client.send(message.encode())

    except:
        pass

    finally:
        # Handle disconnection
        for item in clients:
            if item[0] == client:
                clients.remove(item)
                name = item[1]

                print(name, "disconnected.")

                for other_client, other_name in clients:
                    message = f"[{get_time()}] {name} disconnected."
                    other_client.send(message.encode())

                break

        client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(2)

print("Chat server started.")
print("Waiting for clients...")

while True:
    client, address = server.accept()

    print("Client connected:", address)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()