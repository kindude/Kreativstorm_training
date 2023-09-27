import socket

server_address = ('localhost', 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(server_address)

print(f"UDP is listening on {server_address}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received data from {client_address}: {data.decode()}")
    response = "Server received your message"
    server_socket.sendto(response.encode(), client_address)
