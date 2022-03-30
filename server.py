import threading, socket


class Server:
  def __init__(self) -> None:
      self.clients = []
      self.nicknames = []
      return

  def broadcast(self, message: str) -> None:
    for client in self.clients:
      client.send(message)
    return

  def handle(self, client: socket.socket):
    while True:
      try:
        message = client.recv(1024)
        self.broadcast(message)
      except:
        index = self.clients.index(client)
        self.clients.remove(client)
        client.close()
        nickname = self.nicknames[index]
        self.broadcast(f'{nickname} left chat!'.encode())
        self.nicknames.remove(nickname)
        break

  def receive(self, server):
    while True:
      try: 
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('nickname'.encode())
        nickname = client.recv(1024).decode()
        self.nicknames.append(nickname)
        self.clients.append(client)

        print(f'Nickname ok the client is {nickname}!')
        self.broadcast(f"{nickname} joined the chat!".encode())
        client.send('Connected to the server!'.encode())

        thread = threading.Thread(target=self.handle, args=(client,))
        thread.daemon = True
        thread.start()
      except:
        print("Closing connection!")
        break


if __name__ == '__main__':
  host = '127.0.0.1'
  port = 55555
  try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print("Welcome to the server chat room!")
    print("Waiting for clients...")
    Server().receive(server)
  except ConnectionResetError as e:
    print(f"Connection failed with clients!: {e}")
  except KeyboardInterrupt:
    print("Closing connection!")
  finally:
    server.close()
