# Dilpreet's Chat Room - Server Side
import threading
import socket

host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
aliases = []

print("🌟 Dilpreet's Chatroom Server is LIVE! 🌟")
print(f"📡 Listening for connections on {host}:{port}...\n")


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.close()
            clients.remove(client)
            alias = aliases[index]
            broadcast(f'👋 {alias.decode()} has left the chat room.'.encode('utf-8'))
            aliases.remove(alias)
            break


def receive():
    while True:
        print("💬 Waiting for new connections...")
        client, address = server.accept()
        print(f"✅ Connected with {str(address)}")

        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)

        aliases.append(alias)
        clients.append(client)

        print(f"🏷️  New user joined: {alias.decode()}")
        broadcast(f'🎉 {alias.decode()} has joined Dilpreet\'s Chatroom!'.encode('utf-8'))
        client.send('🌈 You are now connected to Dilpreet\'s Chatroom! Enjoy chatting!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
