import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host = input("(*)Enter Host ip: ")
port = int(input("(*)Enter Port: "))

def port_scanner(port):
    if sock.connect_ex((host,port)):
        print("Port %d is closed" %port)
    else:
        print("Port %d is opened" %port)

port_scanner(port)