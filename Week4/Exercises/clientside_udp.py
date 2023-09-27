import socket

server_address = ('localhost', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a message to the server (or exit to quit): ")
    if message.lower() == 'exit':
        break

    client_socket.sendto(message.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print(f"Received from server: {data.decode()}")

client_socket.close()