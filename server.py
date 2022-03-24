import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 12000))

while True:
  message_bytes, ip_address_server = server.recvfrom(2048)
  message = message_bytes.decode()
  server.sendto(message.encode(), ip_address_server)
  print(message)
