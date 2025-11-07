from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        print(packet.summary())  # Prints a brief summary
        packet.show()            # Displays detailed packet header info

# Sniff packets on localhost (you can change the interface or use a port filter if needed)
sniff(filter="tcp port 80", prn=packet_callback, count=10)
