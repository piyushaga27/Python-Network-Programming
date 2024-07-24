'''
Basic Packet Sniffer

Create a packet sniffer to capture and display network packets.

Task:

    Capture packets on a network interface.
    Display the contents of each packet in a readable format.

Hint: Use the scapy library for packet manipulation and sniffing.
'''

from scapy.all import sniff

def packetCallBack(packet):
    print(f"[*] Packet Captured: {packet.summary()}")
    packet.show()
    print("="*100)

def main():
    interface= "eth0"

    print(f"[*] Starting Packet Sniffer at Interface {interface}...")
    sniff(iface=interface, prn=packetCallBack, store=False)

if __name__=='__main__':
    main()