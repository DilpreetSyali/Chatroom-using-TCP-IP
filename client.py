import threading
import socket

print("╔═══════════════════════════════════════════╗")
print("║     🌸 Welcome to Dilpreet's Chatroom! 🌸║")
print("║    Type your messages and have fun! 🎉    ║")
print("╚═══════════════════════════════════════════╝")

alias = input('👤 Choose your alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('127.0.0.1', 59000))
except:
    print("🚫 Unable to connect to the server. Please make sure the server is running.")
    exit()


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("❗ Error receiving message. Connection closed.")
            client.close()
            break


def client_send():
    while True:
        try:
            message = f'{alias}: {input("")}'
            client.send(message.encode('utf-8'))
        except:
            print("❗ Error sending message. Connection might be closed.")
            break


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
