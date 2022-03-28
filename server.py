import socket


def server(server_connection):
  print(f"Server up and listening port: 12000")
  while True:
    message_bytes, ip_address_server = server_connection.recvfrom(2048)
    print(f"Message from client: {message_bytes.decode()}")
    server_connection.sendto(message_bytes, ip_address_server)
  
if __name__ == "__main__":
  try:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_connection.bind((socket.gethostbyname(socket.gethostname()), 12000))
    server(server_connection)
  except socket.error as e:
    print(f"A socket connecting problem occur: {e}")
  except KeyboardInterrupt as e:
    print("Closing server connection")
  finally:
    server_connection.close()
