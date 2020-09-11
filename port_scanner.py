import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.1.69"
port = 443

def port_scanner(port):
    if sock.connect_ex((host,port)):
        print("Port %d is closed" %port)
    else:
        print("Port %d is opened" %port)

port_scanner(port)