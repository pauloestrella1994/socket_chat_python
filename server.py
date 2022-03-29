import socket


def send_message(server_connection, message_bytes, client):
  server_connection.sendto(message_bytes, client)
  return

def server(server_connection):
  clients = set()
  print(f"Server up and listening port: 12000")
  try:
    while True:
      message_bytes, address_client = server_connection.recvfrom(2048)
      print(f"Message from client: {message_bytes.decode()}")
      clients.add(address_client)
      for client in clients:
        send_message(server_connection,message_bytes, client)
  except socket.error as e:
    print(f"A error occur in socket: {e}")
    server_connection.close()

if __name__ == "__main__":
  try:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server_connection.bind((socket.gethostbyname(socket.gethostname()), 12000))
    server(server_connection)
  except socket.error as e:
    print(f"A socket connecting problem occur: {e}")
  except KeyboardInterrupt as e:
    print("Closing server connection")
  finally:
    server_connection.close()
