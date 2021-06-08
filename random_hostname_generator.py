#!/usr/bin/python3.8
##generate random IP addresses and hostnames
## this is a string generator from regex
## deps: pip install rstr

import socket
import rstr

def random_hosts():
    ip = rstr.xeger(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
    try:
        a = socket.gethostbyaddr(ip)
    except Exception as e:
        return (f"hostname: None   IP: {ip}") 


    return (f"hostname: {a[0]}   IP: {ip}")

if __name__ == '__main__':
    
    for _ in range(500):
        z = random_hosts()
        print(z)