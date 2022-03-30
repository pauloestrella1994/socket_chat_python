import threading, socket


host = '127.0.0.1'
port = 55555
nickname = input("choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
  while True:
    try:
      message = client.recv(1024).decode()
      if message == 'NICK':
        client.send(nickname.encode())
      else:
        print(message)
    except:
      print('An error occurred!')
      client.close()
      break

def write():
  while True:
    message = f'{nickname}: {input("")}'
    client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
