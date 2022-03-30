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

  def receive(self):
    while True:
      client, address = server.accept()
      print(f"Connected with {str(address)}")

      client.send('NICK'.encode())
      nickname = client.recv(1024).decode()
      self.nicknames.append(nickname)
      self.clients.append(client)

      print(f'Nickname ok the client is {nickname}!')
      self.broadcast(f"{nickname} joined the chat!".encode())
      client.send('Connected to the server!'.encode())

      thread = threading.Thread(target=self.handle, args=(client,))
      thread.start()


if __name__ == '__main__':
  host = '127.0.0.1'
  port = 55555
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host, port))
  server.listen()
  print("Welcome to the server chat room!")
  print("Waiting for clients...")
  Server().receive()
