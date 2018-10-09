#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install scapy


"""
[{'name': 'Intel(R) 82574L Gigabit Network Connection',
  'win_index': '4',
  'description': 'Ethernet0',
  'guid': '{28B8F286-XXXX-XXXX-XXXX-XXXXXXXX}',
  'mac': '00:0C:29:XX:YY:ZZ',
  'netid': 'Ethernet0'}]
"""

from pprint import pprint
from scapy.arch.windows import get_windows_if_list
from scapy.all import *


# disable verbose mode
conf.verb = 0


def parse_packet(packet):
    """sniff callback function.
    """
    if packet and packet.haslayer('UDP'):
        # packet.show()
        udp = packet.getlayer('UDP')
        udp.show()
        # if udp.haslayer('Raw'):
        #     data = udp.getlayer('Raw').load
        #     print(data)    # MTU: 1500 = 28 + 1472


def udp_sniffer():
    """start a sniffer.
    """
    interfaces = get_windows_if_list()
    pprint(interfaces)

    print('\n[*] start udp sniffer')
    sniff(
        filter="udp port 53",
        iface=r'Intel(R) 82574L Gigabit Network Connection', prn=parse_packet
    )


if __name__ == '__main__':
    udp_sniffer()
