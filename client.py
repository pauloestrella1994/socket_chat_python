import threading, socket


class Client:
  def receive(self, client: socket.socket):
    while True:
      try:
        message = client.recv(1024).decode()
        if message == 'nickname':
          client.send(nickname.encode())
        if message == 'Server is out!':
          print(message)
          client.close()
          break
        else:
          print(message)
      except:
        print('An error occurred!')
        client.close()
        break

  def write(self, client: socket.socket):
    while True:
      try:
        message = f'{nickname}: {input("")}'
        client.send(message.encode())
      except:
        print('An error occurred!')
        client.close()
        break
        

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 55555
  nickname = input("Choose a nickname: ")
  threads_list = []
  try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client_class = Client()
    receive_thread = threading.Thread(target=client_class.receive, args=(client,))
    receive_thread.daemon = True
    threads_list.append(receive_thread)
    receive_thread.start()

    write_thread = threading.Thread(target=client_class.write, args=(client,))
    write_thread.daemon = True
    threads_list.append(write_thread)
    write_thread.start()

    for thr in threads_list:
      thr.join()
  except:
    print("Closing client!")
    client.close()
