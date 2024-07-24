'''
1. Basic Network Scanner

Create a simple script to scan a range of IP addresses and check which ones are active.

Task:

    Accept a range of IP addresses.
    Ping each IP address in the range.
    Print out which IPs are active.

Hint: Use the os module to run system ping commands.
'''

import os
import subprocess
import platform
import threading

def ping_ip(ip):

    param = "-n" if platform.system().lower() == 'windows' else "-c"
    with open(os.devnull, 'wb') as devnull:
        response= subprocess.call(['ping',param,'1',ip], stdout=devnull , stderr=devnull)
    if response == 0:
        print(f"[*] {ip} is active")
    else:
        print(f"[!] {ip} is not active")

def main():
    subnet = input("Enter the Subnet (e.g., 192.168.1.): ")
    start_ip= int(input("Enter the Start IP (Only Last Octet): "))
    last_ip = int(input("Enter the last IP (Only Last Octet): "))

    threads = []

    for i in range(start_ip, last_ip+1):
        ip = subnet+str(i)
        thread = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
if __name__ == "__main__":
    main()