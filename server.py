import threading, socket


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

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
      client.close()
      nickname = nicknames[index]
      broadcast(f'{nickname} left chat!'.encode())
      nicknames.remove(nickname)
      break

def receive():
  while True:
    client, address = server.accept()
    print(f"Connected with {str(address)}")

    client.send('NICK'.encode())
    nickname = client.recv(1024).decode()
    nicknames.append(nickname)
    clients.append(client)

    print(f'Nickname ok the client is {nickname}!')
    broadcast(f"{nickname} joined the chat!".encode())
    client.send('Connected to the server!'.encode())

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

if __name__ == '__main__':
  print("Welcome to the server chat room!")
  print("Waiting for clients...")
  receive()
