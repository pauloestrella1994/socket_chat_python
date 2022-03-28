import socket


def client(client_connection):
  try:
    while True:
      client_message = input()
      client_connection.sendto(client_message.encode(), (socket.gethostbyname(socket.gethostname()), 12000))
      message_bytes, ip_address_server = client_connection.recvfrom(2048)
      print(f"Receiving message from server: {message_bytes.decode()}")
  except KeyboardInterrupt:
    print(f"Closing client connection with the server ip: {ip_address_server[0]}; port: {ip_address_server[1]}")
  finally:
    client_connection.close()

if __name__ == "__main__":
  try:
    client_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Start connection with the server: {client_connection}")
    client(client_connection)
  except socket.error as e:
    print(f"A socket connecting problem occur: {e}")
  finally:
    client_connection.close()