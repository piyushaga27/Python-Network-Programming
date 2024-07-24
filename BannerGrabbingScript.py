'''
4. Banner Grabbing Script

Write a script to perform banner grabbing to get information from a service running on an open port.

Task:

    Connect to a specified port on a target IP.
    Send a request to get the banner.
    Print the banner information.

Hint: Use the socket module and remember to set a timeout.
'''
'''
import socket

def grabBanner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ip,port))
        banner = sock.recv(1024)

        print(f"[*] Banner from {ip}:{port} - {banner.decode().strip()}")
        sock.close()

    except Exception as e:
        print(f"[!] Error Occured: {e}")

def main():
    ip = input("Enter IP Address: ")
    port = int(input("Enter Port Number: "))

    grabBanner(ip, port)

if __name__ == "__main__":
    main()


'''

import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ip, port))
        sock.send(b'GET / HTTP/1.1\r\n\r\n')
        banner = sock.recv(1024)
        print(f"Banner: {banner.decode().strip()}")
        sock.close()
    except socket.timeout:
        print(f"Connection to {ip}:{port} timed out.")
    except Exception as e:
        print(f"An error Occured: {e}")
    

ip = input("Enter IP Address or host: ")
port = 80
grab_banner(ip, port)
