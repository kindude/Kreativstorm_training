import socket
try:
    hostname = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(hostname)[2]
    print(f"Hostname: {hostname}")
    print("IP addresses")
    for ip in ip_addresses:
        print(ip)

except socket.error as e:
    print(f"Error: {e}")
