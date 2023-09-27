import socket


hostname = '192.168.0.1'

port_list = [53, 80, 8080, 443]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    service_name = "unknown"
    try:
        # s.connect((hostname, port))
        # print(f"Port {port} is open")
        service_name = socket.getservbyport(port)
        s.connect((hostname, port))
        print(f"Port {port} ({service_name}) is open")
    except:
        print(f"Port {port} ({service_name}) is closed")

    s.close()
