import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  client_message = input()
  client.sendto(client_message.encode(), (socket.gethostbyname(socket.gethostname()), 12000))
  message_bytes, ip_address_server = client.recvfrom(2048)
