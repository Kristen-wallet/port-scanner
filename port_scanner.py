import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host = input("[*]Enter Host ip: ")
port_range = int(input("[*]Enter Port range: "))
while port_range > 5000:
    print(colored("[!]Port range must be less than 5000","yellow"))
    port_range = int(input("[*]Enter Port range: "))

def port_scanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!]Port %d is closed" %port ,'red'))
    else:
        print(colored("[+]Port %d is opened" %port, 'green'))

for i in range(1,port_range):
    port_scanner(i)