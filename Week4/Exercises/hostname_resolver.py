import socket

hostname = 'google.com'

try:
    ip_address = socket.gethostbyname(hostname)
    print(f"The Ip address of {hostname} isd {ip_address}")

except socket.error as e:
    print(f"Error: {e}")