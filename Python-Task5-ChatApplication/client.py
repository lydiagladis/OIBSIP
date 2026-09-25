import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

# Send your name to the server
client.send(name.encode())


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                print("\n" + message)

        except:
            print("Disconnected from server.")
            break


# Start a thread to receive messages
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

print("Connected to the chat!")
print("Type your messages below.")
print("Type 'quit' to leave.")

while True:
    message = input()

    if message.lower() == "quit":
        client.close()
        break
    client.send(message.encode())
