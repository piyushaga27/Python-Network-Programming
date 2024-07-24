'''
2. Simple Port Scanner

Write a script that can scan for open ports on a given host.

Task:

    Accept a hostname or IP address.
    Scan a range of ports on the host.
    Print out which ports are open.

Hint: Use the socket module to attempt to connect to each port. 
'''

import socket
import threading

def portScan(host, port):
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)
    result = sock.connect_ex((host,port))

    if result == 0:
        print(f"[*] Port {port} is Open")
     
    
    sock.close()


def main():
    host = input("Enter the Host to scan (Hostname or IP Address): ")

    while True:
        startPort= int(input("Enter the Start Port: "))
        if startPort >= 1 and startPort <= 65535:
            break
        else:
            print("[!] Please Enter the Port Number Range between 1 - 65535")
    while True:    
        endPort= int(input("Enter the End Port: "))
        if endPort >= 1 and endPort <= 65535:
            break
        else:
            print("[!] Please Enter the Port Number Range Between 1 - 65535")

    
    threads = []

    for port in range(startPort, endPort+1):
        thread= threading.Thread(target=portScan, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__=="__main__":
    main()