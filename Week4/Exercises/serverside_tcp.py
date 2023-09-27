import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("", 8081))
server_socket.listen(5)

print("Server is listening on port 8081...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_socket.send(b"Hello, client!")

    client_socket.close()