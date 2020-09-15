#!/usr/bin/python3
from socket import *
import optparse
from threading import *

def connScan(tgtHost , tgtPort):
    try:
        sock = socket(AF_INET , SOCK_STREAM)
        sock.connect_ex((tgtHost,tgtPort))
        print("[+] %d/tcp Opened" %tgtPort)
    except:
        print("[-] %d/tcp Closed" %tgtPort)
    finally:
        sock.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print("[!]Unknown Host %s" %tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("Scan result for : " + tgtName[0])
    except:
        print("Scan result for : " + tgtIp)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan , args=(tgtHost,int(tgtPort)))
        t.start()
    

def main():
    parser = optparse.OptionParser("Usage of program" + "-H <target host> -p <target port>")
    parser.add_option("-H", dest="tgtHost", type="string",help="Specify target host")
    parser.add_option("-p", dest="tgtPorts", type="string",help="Specify target port")
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(",")
    raw = ['None']
    if (tgtPorts== ['None']) or (tgtHost == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)
    
if __name__ == '__main__':
    main()




